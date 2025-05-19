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
    name = strawberry.auto
    serial = strawberry.auto
    asset_tag = strawberry.auto
    status = strawberry.auto
    
    # Filtros para relacionamentos
    device_type = strawberry.auto
    module_type = strawberry.auto
    inventoryitem_type = strawberry.auto
    rack_type = strawberry.auto
    tenant = strawberry.auto
    device = strawberry.auto
    module = strawberry.auto
    contact = strawberry.auto
    inventoryitem = strawberry.auto
    rack = strawberry.auto
    storage_location = strawberry.auto
    owner = strawberry.auto
    delivery = strawberry.auto
    purchase = strawberry.auto


@strawberry_django.filter(models.Supplier, lookups=True)
class SupplierFilter(BaseFilterMixin):
    name = strawberry.auto
    slug = strawberry.auto
    description = strawberry.auto


@strawberry_django.filter(models.Purchase, lookups=True)
class PurchaseFilter(BaseFilterMixin):
    name = strawberry.auto
    status = strawberry.auto
    date = strawberry.auto
    description = strawberry.auto
    supplier = strawberry.auto


@strawberry_django.filter(models.Delivery, lookups=True)
class DeliveryFilter(BaseFilterMixin):
    name = strawberry.auto
    date = strawberry.auto
    description = strawberry.auto
    purchase = strawberry.auto
    receiving_contact = strawberry.auto


@strawberry_django.filter(models.InventoryItemType, lookups=True)
class InventoryItemTypeFilter(BaseFilterMixin):
    model = strawberry.auto
    slug = strawberry.auto
    part_number = strawberry.auto
    description = strawberry.auto
    manufacturer = strawberry.auto
    inventoryitem_group = strawberry.auto


@strawberry_django.filter(models.InventoryItemGroup, lookups=True)
class InventoryItemGroupFilter(BaseFilterMixin):
    name = strawberry.auto
    slug = strawberry.auto
    description = strawberry.auto
    parent = strawberry.auto
