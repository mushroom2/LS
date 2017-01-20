# coding=utf-8
from googleads import adwords
from get_comapings import g_c

CAMPAIGN_ID = 731695173

iplist = ['195.39.210.0', '195.39.210.1', '195.39.210.2', '195.39.210.3', '195.39.210.4',
                '195.39.210.5', '195.39.210.6', '195.39.210.7', '195.39.210.8', '195.39.210.9']

def main(client, campaign_id, ipaddr):
    # Initialize appropriate service.
    campaign_criterion_service = client.GetService(
        'CampaignCriterionService', version='v201609')

    negative_campaign_criterion_operand = {
        'xsi_type': 'NegativeCampaignCriterion',
        'campaignId': campaign_id,
        'criterion': {
            'xsi_type': 'IpBlock',
            'ipAddress': ipaddr
        }
    }

    # Create operations
    operations = [{
                      'operator': 'ADD',
                      'operand': negative_campaign_criterion_operand
                  }]

    # Add the negative campaign criterion.

    # Make the mutate request.
    result = campaign_criterion_service.mutate(operations)

    # Display the resulting campaign criteria.
    for campaign_criterion in result['value']:
        print ('Campaign criterion with campaign id \'%s\', criterion id \'%s\', '
               'and type \'%s\' was added.'
               % (campaign_criterion['campaignId'],
                  campaign_criterion['criterion']['id'],
                  campaign_criterion['criterion']['type']))


if __name__ == '__main__':
    # Initialize client object.
    adwords_client = adwords.AdWordsClient.LoadFromStorage("/home/mushroom/Документы/ls/ya/LS/Google/googleads.yaml")
    campaignidlist = g_c(adwords_client)

for camp in campaignidlist:
    for ipaddr in iplist:
        main(adwords_client, camp, ipaddr)