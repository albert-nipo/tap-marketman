import pytest
from tap_marketman.client import MarketManClient

import os
from dotenv import load_dotenv

load_dotenv()
apikey = os.getenv('APIKey')
apipassword = os.getenv('APIPassword')

@pytest.mark.vcr()
def test_get_auth_token():
    client = MarketManClient(apikey=apikey, apipassword=apipassword)

    assert isinstance(client.auth_token, str)


@pytest.mark.vcr()
def test_get_guid():
    client = MarketManClient(apikey=apikey, apipassword=apipassword)
    guid_list = client.get_guid()

    assert isinstance(guid_list, list)


@pytest.mark.vcr()
def test_get_inventory_items():
    guid = 'edd590e6d4ea4f8fada26bc912c84525'
    client = MarketManClient(apikey=apikey, apipassword=apipassword)
    response = client.get_inventory_items(guid=guid)

    inventory = response['Items']
    for item in inventory:
        assert 'ID' in item
        assert 'Name' in item
        assert 'UpdateDate' in item
        assert 'CategoryID' in item
        assert 'CategoryName' in item
        assert 'UOMName' in item
        assert 'UOMID' in item
        assert 'MinOnHand' in item
        assert 'ParLevel' in item
        assert 'StorageNames' in item
        if len(item['StorageNames']) > 0:
            assert isinstance(item['StorageNames'][0], str)

        assert 'StorageIDs' in item
        if len(item['StorageIDs']) > 0:
            assert isinstance(item['StorageIDs'][0], int)

        assert 'OnHand' in item
        assert 'BOMPrice' in item
        assert 'DebitAccountName' in item
        assert 'PurchaseItems' in item
        if len(item['PurchaseItems']) > 0:
            for PItem in item['PurchaseItems']:
                assert 'Name' in PItem
                assert 'SupplierName' in PItem
                assert 'VendorName' in PItem
                assert 'PackQty' in PItem
                assert 'PacksPerCase' in PItem
                assert 'UOMName' in PItem
                assert 'UOMID' in PItem
                assert 'ProductCode' in PItem
                assert 'Price' in PItem
                assert 'MinOrderQty' in PItem
                assert 'PriceType' in PItem
                assert 'Ratio' in PItem
                assert 'VendorGuid' in PItem
                assert 'CatalogItemCode' in PItem
                assert 'TaxLevelID' in PItem
                assert 'TaxValue' in PItem
                assert 'PriceWithVat' in PItem
                assert 'ScanBarcode' in PItem

        assert 'IsDeleted' in item


@pytest.mark.vcr()
def test_get_inventory_counts():
    guid = 'edd590e6d4ea4f8fada26bc912c84525'
    client = MarketManClient(apikey=apikey, apipassword=apipassword)
    response = client.get_inventory_counts(guid=guid, 
                                           start_time='2019/01/01 00:00:00', 
                                           end_time='2019/01/07 00:00:00')

    inventory_counts = response['InventoryCounts']
    if len(inventory_counts) > 0:
        for inventory_count in inventory_counts:
            assert 'BuyerGuid' in inventory_count
            assert 'BuyerName' in inventory_count
            # This is how comments is spelled in the API
            assert 'Commments' in inventory_count
            assert 'CountDateUTC' in inventory_count
            assert 'ID' in inventory_count
            assert 'PriceTotalWithoutVAT' in inventory_count
            assert 'Lines' in inventory_count
            if len(inventory_count['Lines']) > 0:
                for line in inventory_count['Lines']:
                    assert 'ItemID' in line
                    assert 'ItemName' in line
                    assert 'LineID' in line
                    assert 'TotalCount' in line
                    assert 'TotalValue' in line


@pytest.mark.vcr()
def test_get_menu_items():
    guid = '0b0a566dc9704123bb603be77a085098'
    client = MarketManClient(apikey=apikey, apipassword=apipassword)
    response = client.get_menu_items(guid=guid)

    menu_items = response['Items']
    if len(menu_items) > 0:
        for item in menu_items:
            assert 'ID' in item
            assert 'Name' in item
            assert 'CategoryID' in item
            assert 'CategoryName' in item
            assert 'POSCodes' in item
            assert 'SalePriceWithoutVAT' in item
            assert 'SalePriceWithVAT' in item
            assert 'Type' in item
            assert 'MinOnHand' in item
            assert 'ParLevel' in item
            assert 'BOMPrice' in item
            assert 'BOMPriceFC' in item
            assert 'MaxFC' in item
            assert 'PrepTime' in item
            assert 'CookTime' in item
            assert 'CookingInstructions' in item
            assert 'AboutTheItem' in item
            assert 'SubItems' in item
            if len(item['SubItems']) > 0:
                for sub_item in item['SubItems']:
                    assert 'ItemID' in sub_item
                    assert 'ItemName' in sub_item
                    assert 'ItemTypeName' in sub_item
                    assert 'UsageNet' in sub_item
                    assert 'LossPercent' in sub_item
                    assert 'ActualUsage' in sub_item

            assert 'IsDeleted' in item


@pytest.mark.vcr()
def test_get_preps():
    guid = '0b0a566dc9704123bb603be77a085098'
    client = MarketManClient(apikey=apikey, apipassword=apipassword)
    response = client.get_preps(guid=guid)

    items = response['Items']
    if len(items) > 0:
        for item in items:
            assert 'ID' in item
            assert 'Name' in item
            assert 'IsSelfStock' in item
            assert 'CategoryID' in item
            assert 'CategoryName' in item
            assert 'UOMName' in item
            assert 'UOMID' in item
            assert 'MinOnHand' in item
            assert 'ParLevel' in item
            assert 'StorageNames' in item
            if len(item['StorageNames']) > 0:
                assert isinstance(item['StorageNames'][0], str)

            assert 'StorageIDs' in item
            if len(item['StorageIDs']) > 0:
                assert isinstance(item['StorageIDs'][0], int)

            assert 'ProdQuantity' in item
            assert 'OnHand' in item
            assert 'BOMPrice' in item
            assert 'SubItems' in item
            if len(item['SubItems']) > 0:
                for sub_item in item['SubItems']:
                    assert 'ItemID' in sub_item
                    assert 'ItemName' in sub_item
                    assert 'ItemTypeName' in sub_item
                    assert 'UsageNet' in sub_item
                    assert 'LossPercent' in sub_item
                    assert 'ActualUsage' in sub_item

            assert 'UpdateDate' in item
            assert 'IsDeleted' in item


@pytest.mark.vcr()
def test_get_transfers():
    guid = '0b0a566dc9704123bb603be77a085098'
    client = MarketManClient(apikey=apikey, apipassword=apipassword)
    response = client.get_transfers(guid=guid, 
                                    start_time='2019/01/01 00:00:00', 
                                    end_time='2020/01/07 00:00:00')

    transfers = response['Transfers']
    if len(transfers) > 0:
        for transfer in transfers:
            assert 'ID' in transfer
            assert 'BuyerFromName' in transfer
            assert 'BuyerFromGuid' in transfer
            assert 'BuyerToName' in transfer
            assert 'BuyerToGuid' in transfer
            assert 'DateUTC' in transfer
            assert 'TotalPriceWithoutVAT' in transfer
            assert 'Commments' in transfer
            assert 'TransferStatus' in transfer
            assert 'Lines' in transfer
            if len(transfer['Lines']) > 0:
                for line in transfer['Lines']:
                    assert 'ItemID' in line
                    assert 'ItemName' in line
                    assert 'LineID' in line
                    assert 'Quantity' in line
                    assert 'TotalPriceWithoutVAT' in line
                    assert 'UOMID' in line
                    assert 'UOMName' in line


@pytest.mark.vcr()
def test_get_waste_events():
    guid = '0b0a566dc9704123bb603be77a085098'
    client = MarketManClient(apikey=apikey, apipassword=apipassword)
    response = client.get_waste_events(guid=guid,
                                      start_time='2019/01/01 00:00:00',
                                      end_time='2019/01/07 00:00:00')

    waste_events = response['WasteEvents']
    if len(waste_events) > 0:
        for event in waste_events:
            assert 'ID' in event
            assert 'BuyerName' in event
            assert 'BuyerGuid' in event
            assert 'DateUTC' in event
            assert 'TotalPriceWithoutVAT' in event
            assert 'Commments' in event
            assert 'Lines' in event
            if len(event['Lines']) > 0:
                for line in event['Lines']:
                    assert 'LineID' in line
                    assert 'ItemID' in line
                    assert 'ItemName' in line
                    assert 'Quantity' in line
                    assert 'TotalPriceWithoutVAT' in line
                    assert 'UOMID' in line
                    assert 'UOMName' in line


@pytest.mark.vcr()
def test_get_orders_by_sent_date():
    guid = '0b0a566dc9704123bb603be77a085098'
    client = MarketManClient(apikey=apikey, apipassword=apipassword)
    response = client.get_orders_by_sent_date(guid=guid,
                                              start_time='2019/01/01 00:00:00',
                                              end_time='2019/01/07 00:00:00')

    orders = response['Orders']
    if len(orders) > 0:
        for order in orders:
            assert 'OrderNumber' in order
            assert 'VendorName' in order
            assert 'VendorGuid' in order
            assert 'BuyerName' in order
            assert 'BuyerGuid' in order
            assert 'Comments' in order
            assert 'PriceTotalWithoutVAT' in order
            assert 'PriceTotalWithVAT' in order
            assert 'SentDateUTC' in order
            assert 'OrderStatus' in order
            assert 'DeliveryDateUTC' in order
            assert 'Items' in order
            if len(order['Items']) > 0:
                for item in order['Items']:
                    assert 'ItemName' in item
                    assert 'SKU' in item
                    assert 'Quantity' in item
                    assert 'Price' in item
                    assert 'PriceTotal' in item
                    assert 'BarcodeManufacture' in item
                    assert 'CatalogItemID' in item
                    assert 'CatalogItemCode' in item
                    assert 'TaxLevelID' in item
                    assert 'TaxValue' in item
                    assert 'PriceTotalWithVat' in item
                    assert 'ItemMeasureTypeID' in item
                    assert 'ItemMeasureTypeName' in item
                    assert 'PackQuantity' in item
                    assert 'PacksPerCase' in item


@pytest.mark.vcr()
def test_get_vendors():
    client = MarketManClient(apikey=apikey, apipassword=apipassword)
    response = client.get_vendors()

    vendors = response['Vendors']
    if len(vendors) > 0:
        for vendor in vendors:
            assert 'VendorName' in vendor
            assert 'VendorGuid' in vendor

