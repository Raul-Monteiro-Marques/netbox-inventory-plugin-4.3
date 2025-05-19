import strawberry
import strawberry_django

from netbox.graphql.filter_mixins import BaseFilterMixin

from netbox_inventory import filtersets, models

__all__ = (
    'AssetFilter',
    'SupplierFilter',
    'PurchaseFilter',
    'DeliveryFilter',
    'InventoryItemTypeFilter',
    'InventoryItemGroupFilter',
)


@strawberry_django.filter(models.Asset, lookups=True)
class AssetFilter(BaseFilterMixin):
    # Filtros específicos para Asset
    name = strawberry_django.filters.FilterField(lookups=True)
    serial = strawberry_django.filters.FilterField(lookups=True)
    asset_tag = strawberry_django.filters.FilterField(lookups=True)
    status = strawberry_django.filters.FilterField(lookups=True)
    
    # Filtros para relacionamentos
    device_type = strawberry_django.filters.FilterField(lookups=True)
    module_type = strawberry_django.filters.FilterField(lookups=True)
    inventoryitem_type = strawberry_django.filters.FilterField(lookups=True)
    rack_type = strawberry_django.filters.FilterField(lookups=True)
    tenant = strawberry_django.filters.FilterField(lookups=True)
    device = strawberry_django.filters.FilterField(lookups=True)
    module = strawberry_django.filters.FilterField(lookups=True)
    contact = strawberry_django.filters.FilterField(lookups=True)
    inventoryitem = strawberry_django.filters.FilterField(lookups=True)
    rack = strawberry_django.filters.FilterField(lookups=True)
    storage_location = strawberry_django.filters.FilterField(lookups=True)
    owner = strawberry_django.filters.FilterField(lookups=True)
    delivery = strawberry_django.filters.FilterField(lookups=True)
    purchase = strawberry_django.filters.FilterField(lookups=True)


@strawberry_django.filter(models.Supplier, lookups=True)
class SupplierFilter(BaseFilterMixin):
    name = strawberry_django.filters.FilterField(lookups=True)
    slug = strawberry_django.filters.FilterField(lookups=True)
    description = strawberry_django.filters.FilterField(lookups=True)


@strawberry_django.filter(models.Purchase, lookups=True)
class PurchaseFilter(BaseFilterMixin):
    name = strawberry_django.filters.FilterField(lookups=True)
    status = strawberry_django.filters.FilterField(lookups=True)
    date = strawberry_django.filters.FilterField(lookups=True)
    description = strawberry_django.filters.FilterField(lookups=True)
    supplier = strawberry_django.filters.FilterField(lookups=True)


@strawberry_django.filter(models.Delivery, lookups=True)
class DeliveryFilter(BaseFilterMixin):
    name = strawberry_django.filters.FilterField(lookups=True)
    date = strawberry_django.filters.FilterField(lookups=True)
    description = strawberry_django.filters.FilterField(lookups=True)
    purchase = strawberry_django.filters.FilterField(lookups=True)
    receiving_contact = strawberry_django.filters.FilterField(lookups=True)


@strawberry_django.filter(models.InventoryItemType, lookups=True)
class InventoryItemTypeFilter(BaseFilterMixin):
    model = strawberry_django.filters.FilterField(lookups=True)
    slug = strawberry_django.filters.FilterField(lookups=True)
    part_number = strawberry_django.filters.FilterField(lookups=True)
    description = strawberry_django.filters.FilterField(lookups=True)
    manufacturer = strawberry_django.filters.FilterField(lookups=True)
    inventoryitem_group = strawberry_django.filters.FilterField(lookups=True)


@strawberry_django.filter(models.InventoryItemGroup, lookups=True)
class InventoryItemGroupFilter(BaseFilterMixin):
    name = strawberry_django.filters.FilterField(lookups=True)
    slug = strawberry_django.filters.FilterField(lookups=True)
    description = strawberry_django.filters.FilterField(lookups=True)
    parent = strawberry_django.filters.FilterField(lookups=True)
