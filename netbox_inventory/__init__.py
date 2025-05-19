from importlib import metadata

from django.db.models.signals import post_migrate
from django.dispatch import receiver
from netbox.plugins import PluginConfig
from packaging import version

from .version import __version__

__all__ = (
    '__version__',
)


class NetBoxInventoryConfig(PluginConfig):
    """This is our custom plugin configuration."""

    name = 'netbox_inventory'
    verbose_name = 'NetBox Inventory'
    description = 'Inventory asset management in NetBox'
    version = __version__
    author = 'Matej Vadnjal'
    author_email = 'matej.vadnjal@arnes.si'
    base_url = 'inventory'
    min_version = '4.3.0'
    max_version = '4.3.99'
    required_settings = []
    default_settings = {
        'top_level_menu': True,
        'used_status_name': 'used',
        'used_additional_status_names': [],
        'stored_status_name': 'stored',
        'stored_additional_status_names': [
            'retired',
        ],
        'sync_hardware_serial_asset_tag': False,
        'asset_import_create_purchase': False,
        'asset_import_create_device_type': False,
        'asset_import_create_module_type': False,
        'asset_import_create_inventoryitem_type': False,
        'asset_import_create_rack_type': False,
        'asset_import_create_tenant': False,
        'asset_disable_editing_fields_for_tags': {},
        'asset_disable_deletion_for_tags': [],
        'asset_custom_fields_search_filters': {},
        'asset_warranty_expire_warning_days': 90,
        'prefill_asset_name_create_inventoryitem': False,
        'prefill_asset_tag_create_inventoryitem': False,
    }
    caching_config = {}
    
    def ready(self):
        super().ready()
        from . import signals  # noqa: F401
        
    def validate(self, data):
        # Validate plugin settings
        errors = []
        
        # Check if any required settings are missing
        for setting in self.required_settings:
            if setting not in data:
                errors.append(
                    f"Required setting '{setting}' is missing."
                )
        
        # Check if NetBox version is compatible
        try:
            import netbox.version
            current_version = version.parse(netbox.version.VERSION)
            min_version = version.parse(self.min_version)
            max_version = version.parse(self.max_version)
            
            if current_version < min_version or current_version > max_version:
                errors.append(
                    f"NetBox version {netbox.version.VERSION} is not compatible with this plugin. "
                    f"This plugin requires NetBox version {self.min_version} to {self.max_version}."
                )
        except (ImportError, AttributeError):
            errors.append(
                "Unable to determine NetBox version."
            )
        
        return errors


config = NetBoxInventoryConfig()


@receiver(post_migrate)
def create_custom_fields(sender, **kwargs):
    """
    Create a custom field to store the asset on device, module, inventory item and rack.
    """
    try:
        from extras.models import CustomField
        from django.contrib.contenttypes.models import ContentType
    except ImportError:
        # Skip if we're missing dependencies (e.g. if we're running tests)
        return

    # Don't create custom fields if we're not running the inventory plugin
    try:
        metadata.distribution('netbox_inventory')
    except metadata.PackageNotFoundError:
        return

    # Don't create custom fields if we're not running the inventory plugin
    if sender.name != 'netbox_inventory':
        return

    # Create custom fields for device, module, inventory item and rack
    for model_name in ('device', 'module', 'inventoryitem', 'rack'):
        # Get the content type for the model
        try:
            content_type = ContentType.objects.get(app_label='dcim', model=model_name)
        except ContentType.DoesNotExist:
            continue

        # Create the custom field if it doesn't exist
        CustomField.objects.get_or_create(
            name='assigned_asset',
            defaults={
                'type': 'object',
                'object_type': ContentType.objects.get(
                    app_label='netbox_inventory', model='asset'
                ),
                'label': 'Asset',
                'description': 'Asset assigned to this {}'.format(model_name),
            },
        )[0].content_types.add(content_type)
