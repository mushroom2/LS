# coding=utf-8

# {"data":{"Password":"EEXuTmL0","FIO":"Vasiliy Pupkin","Email":"test1@yandex.ru","Login":"test1","ClientID":"43873"}}
# {"data":{"Login":"test2","ClientID":"43874","FIO":"John Smith","Password":"C6HrDxMu","Email":"test2@yandex.ru"}}
# {"data":{"FIO":"Wolfgang Mozart","Password":"jwJz0B4a","Login":"test3","Email":"test3@yandex.ru","ClientID":"43875"}}

import json
import urllib2


class MyYandexDirectApi:
    # Initializations
    urlv5 = 'https://api-sandbox.direct.yandex.com/json/v5/'
    urlv4l = 'https://api-sandbox.direct.yandex.ru/live/v4/json/'
    tokenv5 = 'Bearer AQAAAAAa-BvqAAP0fRaW_IXzvUO7rqvPDojV67k'
    tokenv4 = 'AQAAAAAa-BvqAAP0fRaW_IXzvUO7rqvPDojV67k'
    login = 'python.avi'  # Your current login on Yandex Direct

    def get_client_info(self, clientusername):
        # get Client information. Method based on Yandex Direct API Version 5. Client's login is required param
        # example: get_client_info('test1')

        data = {
            'method': 'get',
            'params': {
                "FieldNames": ["ClientId", "Phone", "Login", "Type", "ClientInfo"]
            }
        }
        jdata = json.dumps(data, ensure_ascii=False).encode('utf8')
        req = urllib2.Request(self.urlv5 + 'clients', jdata,
                              headers={"Authorization": self.tokenv5, "Client-Login": clientusername,
                                       'Content-Type': 'application/json; charset=utf-8'})
        self.response = urllib2.urlopen(req)

    def get_client_list(self):
        # get Clients list for your account on Yandex Direct. Method based on Yandex Direct API Version 4 life.

        data = {
            'method': 'GetClientsList',
            'token': self.tokenv4,
            # 'param': []
        }
        jdata = json.dumps(data, ensure_ascii=False).encode('utf8')
        self.response = urllib2.urlopen(self.urlv4l, jdata)

    def add_subclient(self, login, name, surname):
        # add new subclient for your account on Yandex Direct. Method based on Yandex Direct API Version 4 life.
        # method required Login, Name, Surname of NEW subclient

        data = {
            'method': 'CreateNewSubclient',
            'token': self.tokenv4,
            'param': {
                "Login": login,
                "Name": name,
                "Surname": surname
            }
        }
        jdata = json.dumps(data, ensure_ascii=False).encode('utf8')
        self.response = urllib2.urlopen(self.urlv4l, jdata)

    def get_balance(self, campaningid):  # id 180669 180670 180671
        # get balance for marketing campaign. Method based on Yandex Direct API Version 4 life.
        # campaign id is required
        # example: get_balance(180669)

        data = {
            'method': 'GetBalance',
            'token': self.tokenv4,
            'param': [campaningid]
        }
        jdata = json.dumps(data, ensure_ascii=False).encode('utf8')
        self.response = urllib2.urlopen(self.urlv4l, jdata)

    def get_campaign_balance(self, clientusername):  # sbx-pythonoI0dSg
        # Get balance, name, id of marketing campaign, for client or subclient.
        # Method based on Yandex Direct API Version 5.
        # Client's login is required param
        # Method can be extended. More information:
        # 'https://tech.yandex.ru/direct/doc/ref-v5/campaigns/get-docpage/'

        data = {
            'method': 'get',
            'params': {
                "SelectionCriteria": {},
                "FieldNames": ['Name', 'Id', 'Funds'],

            }
        }
        jdata = json.dumps(data, ensure_ascii=False).encode('utf8')
        req = urllib2.Request(self.urlv5 + 'campaigns', jdata,
                              headers={"Authorization": self.tokenv5, "Client-Login": clientusername,
                                       'Content-Type': 'application/json; charset=utf-8'})
        self.response = urllib2.urlopen(req)
        self.jresponse = json.load(self.response, encoding='utf8')

        try:
            for field in self.jresponse['result']['Campaigns']:
                print 'Name =', field['Name'], ', Id =', field['Id'], ', Balance =', field['Funds']['CampaignFunds'][
                    'Balance'], ';'
        except KeyError:
            print self.jresponse

    def print_result(self):
        print self.response.read().decode('utf8')


if __name__ == '__main__':
    res = MyYandexDirectApi()
    res.get_campaign_balance('sbx-pythonoI0dSg')

