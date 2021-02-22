import singer
from datetime import datetime, timezone, timedelta

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
        current_guid = guid
        response = self.client.get_inventory_items(guid=current_guid)
        inventory_items = response['Items']

        for inventory_item in inventory_items:
            inventory_item['GUID'] = current_guid
            yield inventory_item


class MenuItem(FullTableStream):
    tap_stream_id = 'menu_item'
    key_properties = ['ID']
    object_type = 'MenuItem'

    def records_sync(self, guid):
        current_guid = guid
        LOGGER.info(f'Sync Menu Items for GUID: {current_guid}')
        response = self.client.get_menu_items(guid=current_guid)
        menu_items = response['Items']

        for menu_item in menu_items:
            menu_item['GUID'] = current_guid
            yield menu_item


class Prep(FullTableStream):
    tap_stream_id = 'prep'
    key_properties = ['ID']
    object_type = 'Prep'

    def records_sync(self, guid):
        current_guid = guid
        LOGGER.info(f'Sync Prep Items for GUID: {current_guid}')
        response = self.client.get_preps(guid=current_guid)
        preps = response['Items']

        for prep in preps:
            prep['GUID'] = current_guid
            yield prep


class Vendor(FullTableStream):
    tap_stream_id = 'vendor'
    key_properties = ['VendorGuid']
    object_type = 'Vendor'

    def records_sync(self, **kwargs):
        response = self.client.get_vendors()
        vendors = response['Vendors']
        for vendor in vendors:
            yield vendor


class InventoryCount(FullTableStream):
    tap_stream_id = 'inventory_count'
    key_properties = ['ID']
    object_type = 'InventoryCount'

    def records_sync(self, guid):
        current_guid = guid
        LOGGER.info(f'Sync Inventory Count for GUID: {current_guid}')
        start_time = singer.get_bookmark(self.state,
                                         self.tap_stream_id,
                                         current_guid)
        if start_time == None:
            start_time = '2019/01/01 00:00:00'

        end_time = datetime.now(timezone.utc).strftime("%Y/%m/%d %H:%M:%S")
        LOGGER.info(
            f'Start time is: {start_time} and the end time is: {end_time}')

        response = self.client.get_inventory_counts(guid=current_guid,
                                                    start_time=start_time,
                                                    end_time=end_time)
        inventory_counts = response['InventoryCounts']
        for inventory_count in inventory_counts:
            inventory_count['GUID'] = current_guid
            yield inventory_count


class Transfer(FullTableStream):
    tap_stream_id = 'transfer'
    key_properties = ['ID']
    object_type = 'Transfer'

    def records_sync(self, guid):
        current_guid = guid
        LOGGER.info(f'Sync Transfer for GUID: {current_guid}')
        start_time = singer.get_bookmark(self.state,
                                         self.tap_stream_id,
                                         current_guid)
        if start_time == None:
            start_time = '2019/01/01 00:00:00'

        end_time = datetime.now(timezone.utc).strftime("%Y/%m/%d %H:%M:%S")
        LOGGER.info(
            f'Start time is: {start_time} and the end time is: {end_time}')

        response = self.client.get_transfers(guid=current_guid,
                                             start_time=start_time,
                                             end_time=end_time)
        transfers = response['Transfers']
        for transfer in transfers:
            transfer['GUID'] = current_guid
            yield transfer


class WasteEvent(FullTableStream):
    tap_stream_id = 'waste_event'
    key_properties = ['ID']
    object_type = 'WasteEvent'

    def records_sync(self, guid):
        current_guid = guid
        LOGGER.info(f'Sync Waste Events for GUID: {current_guid}')
        start_time = singer.get_bookmark(self.state,
                                         self.tap_stream_id,
                                         current_guid)
        if start_time == None:
            start_time = '2019/01/01 00:00:00'

        end_time = datetime.now(timezone.utc).strftime("%Y/%m/%d %H:%M:%S")
        LOGGER.info(
            f'Start time is: {start_time} and the end time is: {end_time}')

        response = self.client.get_waste_events(guid=current_guid,
                                                start_time=start_time,
                                                end_time=end_time)
        waste_events = response['WasteEvents']
        for waste_event in waste_events:
            waste_event['GUID'] = current_guid
            yield waste_event


class OrderBySentDate(FullTableStream):
    tap_stream_id = 'order_by_sent_date'
    key_properties = ['OrderNumber']
    object_type = 'OrderBySentDate'

    def records_sync(self, guid):
        current_guid = guid
        start_time = singer.get_bookmark(self.state,
                                         self.tap_stream_id,
                                         current_guid['orders'])
        if start_time == None:
            start_time = '2019/01/01 00:00:00'
        # end_time = start_time + 14 days
        
        start_time = datetime.strptime(start_time, "%Y/%m/%d %H:%M:%S")
        end_time = start_time + timedelta(days=14)
        LOGGER.info(
            f'Start time is: {start_time} and the end time is: {end_time}')
        while start_time <= datetime.now():
            LOGGER.info(f'Syncing Orders from {start_time} to {end_time} for {current_guid}')
            response = self.client.get_orders_by_sent_date(guid=current_guid,
                                                           start_time=datetime.strftime(
                                                               start_time, "%Y/%m/%d %H:%M:%S"),
                                                           end_time=datetime.strftime(
                                                               end_time, "%Y/%m/%d %H:%M:%S"))
            start_time = end_time
            end_time = start_time + timedelta(days=14)
            orders = response['Orders']
            for order in orders:
                order['GUID'] = current_guid
                yield order

            singer.write_bookmark(
                self.state,
                self.tap_stream_id,
                current_guid['orders'],
                start_time
            )
            singer.write_state(self.state)


STREAMS = {
    'inventory_item': InventoryItem,
    'menu_item': MenuItem,
    'prep': Prep,
    'vendor': Vendor,
    'inventory_count': InventoryCount,
    'transfer': Transfer,
    'waste_event': WasteEvent,
    'order_by_sent_date': OrderBySentDate
}
