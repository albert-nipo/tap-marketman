import json


def create_guid_list(guid_data):
    buyers = extract_guid_buyers(guid_data)
    vendors = extract_guid_vendors(guid_data)
    chains = extract_guid_chains(guid_data)

    guid_list = buyers + vendors + chains

    return guid_list


def extract_guid_buyers(guid_data):
    guid_list = []

    if len(guid_data['Buyers']) == 0:
        return guid_list
    
    for buyer in guid_data['Buyers']:
        guid_list.append(buyer['Guid'])
        
    return guid_list


def extract_guid_vendors(guid_data):
    guid_list = []

    if len(guid_data['Vendors']) == 0:
        return guid_list

    for vendor in guid_data['Vendors']:
        guid_list.append(vendor['Guid'])

    return guid_list


def extract_guid_chains(guid_data):
    guid_list = []

    if len(guid_data['Chains']) == 0:
        return guid_list

    for chain in guid_data['Chains']:
        guid_list.append(chain['Guid'])
    
    for buyer in guid_data['Chains'][0]['Buyers']:
        guid_list.append(buyer['Guid'])

    return guid_list
