# coding=utf-8
from googleads import adwords


PAGE_SIZE = 500



def main(client):
    # Initialize appropriate service.
    ad_group_criterion_service = client.GetService(
        'CampaignCriterionService', version='v201605')

    # Construct selector and get all ad group criteria.
    offset = 0
    selector = {
        'fields': ['IpAddress', 'CampaignId'],

        'predicates': [{
                           'field': 'CriteriaType',
                           'operator': 'IN',
                           'values': ['IP_BLOCK']
                       }]
    }

    page = ad_group_criterion_service.get(selector)

    more_pages = True

    while more_pages:
        page = ad_group_criterion_service.get(selector)
        # Display results.
        if 'entries' in page:
            for ip in page['entries']:
                print (
                    ip['criterion']['ipAddress'],
                    ip['campaignId']
                    )

        else:
            print 'No keywords were found.'
        offset += PAGE_SIZE
        more_pages = offset < int(page['totalNumEntries'])


if __name__ == '__main__':
    # Initialize client object.
    adwords_client = adwords.AdWordsClient.LoadFromStorage("/home/mushroom/Документы/ls/ya/LS/Google/googleads.yaml")

main(adwords_client)