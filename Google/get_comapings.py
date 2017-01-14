#!/usr/bin/python
# coding=utf-8


import logging
import time
from googleads import adwords

logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.transport').setLevel(logging.DEBUG)

PAGE_SIZE = 100


def g_c(client):
    # Initialize appropriate service.
    campaign_service = client.GetService('CampaignService', version='v201609')

    # Construct selector and get all campaigns.
    offset = 0
    selector = {
        'fields': ['Id', 'Name', 'Status'],
        'paging': {
            'startIndex': str(offset),
            'numberResults': str(PAGE_SIZE)
        }
    }

    more_pages = True
    while more_pages:
        page = campaign_service.get(selector)

        # Display results.
        if 'entries' in page:
            campaignidlist = []
            for campaign in page['entries']:
                campaignidlist.append(campaign['id'])
#                print ('Campaign with id \'%s\', name \'%s\', and status \'%s\' was '
#                       'found.'  % (campaign['id'], campaign['name'],
#                                   campaign['status']))


        else:
            print 'No campaigns were found.'
            campaignidlist = []
        offset += PAGE_SIZE
        selector['paging']['startIndex'] = str(offset)
        more_pages = offset < int(page['totalNumEntries'])
#        time.sleep(1)
        return campaignidlist

if __name__ == '__main__':
    adwords_client = adwords.AdWordsClient.LoadFromStorage(
        "/home/mushroom/Документы/ls/ya/LS/Google/googleads.yaml")  # Path to googleads.yaml
    g_c(adwords_client)
