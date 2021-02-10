import singer

LOGGER = singer.get_logger()

class Stream:
    tap_stream_id = None
    key_properties = []
    replication_method = ''
    valid_replication_keys = []
    replication_key = ''
    object_type = ''

    def __init__(self, client, state):
        self.client = client
        self.state = state


class CatalogStream(Stream):
    replication_method = 'INCREMENTAL'


class FullTableStream(Stream):
    replication_method = 'FULL_TABLE'


class InventoryItem(FullTableStream):
    tap_stream_id = 'inventory_item'
    key_properties = ['ID']
    object_type = 'InventoryItem'

    def records_sync(self, guid):
        bookmark_value = singer.get_bookmark(
            self.state,
            self.tap_stream_id,
            self.key_properties[0]
        )

        current_guid=guid
        response = self.client.get_inventory_items(guid=current_guid)
        inventory_items = response['Items']

        for inventory_item in inventory_items:
            yield inventory_item


class MenuItem(FullTableStream):
    tap_stream_id = 'menu_item'
    key_properties = ['ID']
    object_type = 'MenuItem'

    def records_sync(self, guid):
        bookmark_value = singer.get_bookmark(
            self.state,
            self.tap_stream_id,
            self.key_properties[0]
        )

        current_guid = guid
        response = self.client.get_menu_items(guid=current_guid)
        menu_items = response['Items']

        for menu_item in menu_items:
            yield menu_item


class Prep(FullTableStream):
    tap_stream_id = 'prep'
    key_properties = ['ID']
    object_type = 'Prep'

    def records_sync(self, guid):
        bookmark_value = singer.get_bookmark(
            self.state,
            self.tap_stream_id,
            self.key_properties[0]
        )

        current_guid = guid
        response = self.client.get_preps(guid=current_guid)
        preps = response['Items']

        for prep in preps:
            yield prep


class Vendor(FullTableStream):
    tap_stream_id = 'vendor'
    key_properties = ['VendorGuid']
    object_type = 'Vendor'

    def records_sync(self, **kwargs):
        bookmark_value = singer.get_bookmark(
            self.state,
            self.tap_stream_id,
            self.key_properties[0]
        )

        response = self.client.get_vendors()
        vendors = response['Vendors']

        for vendor in vendors:
            yield vendor

STREAMS = {
    'inventory_item': InventoryItem,
    'menu_item': MenuItem,
    'prep': Prep,
    'vendor': Vendor
}
