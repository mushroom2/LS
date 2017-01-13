# coding=utf-8
from googleads import adwords


CAMPAIGN_ID = 731695173


def main(client, campaign_id, location_feed_id=None):
    # Initialize appropriate service.
    campaign_criterion_service = client.GetService(
        'CampaignCriterionService', version='v201609')

    negative_campaign_criterion_operand = {
        'xsi_type': 'NegativeCampaignCriterion',
        'campaignId': campaign_id,
        'criterion': {
            'xsi_type': 'IpBlock',
            'ipAddress': '1.3.8.0/24'
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

main(adwords_client, CAMPAIGN_ID)