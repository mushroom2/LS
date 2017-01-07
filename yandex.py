# coding=utf-8

# {"data":{"Password":"EEXuTmL0","FIO":"Vasiliy Pupkin","Email":"test1@yandex.ru","Login":"test1","ClientID":"43873"}}
# {"data":{"Login":"test2","ClientID":"43874","FIO":"John Smith","Password":"C6HrDxMu","Email":"test2@yandex.ru"}}
# {"data":{"FIO":"Wolfgang Mozart","Password":"jwJz0B4a","Login":"test3","Email":"test3@yandex.ru","ClientID":"43875"}}

import json
import urllib2
import requests


class MyYandexDirectApi:
    urlv5 = 'https://api-sandbox.direct.yandex.com/json/v5/'
    urlv4l = 'https://api-sandbox.direct.yandex.ru/live/v4/json/'
    tokenv5 = 'Bearer AQAAAAAa-BvqAAP0fRaW_IXzvUO7rqvPDojV67k'
    tokenv4 = 'AQAAAAAa-BvqAAP0fRaW_IXzvUO7rqvPDojV67k'
    login = 'python.avi'

    def get_client_info(self, clientusername):
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
        data = {
            'method': 'GetClientsList',
            'token': self.tokenv4,
            # 'param': []
        }
        jdata = json.dumps(data, ensure_ascii=False).encode('utf8')
        self.response = urllib2.urlopen(self.urlv4l, jdata)

    def add_subclient(self, login, name, surname):
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

    def get_ballance(self, campaningid):  # id 180669 180670 180671
        data = {
            'method': 'GetBalance',
            'token': self.tokenv4,
            'param': [campaningid]
        }
        jdata = json.dumps(data, ensure_ascii=False).encode('utf8')
        self.response = urllib2.urlopen(self.urlv4l, jdata)

    def get_camaning(self, clientusername):  # sbx-pythonoI0dSg
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
        for field in self.jresponse['result']['Campaigns']:
            print 'Name =', field['Name'], ', Id =', field['Id'], ', Balance =', field['Funds']['CampaignFunds'][
                'Balance'], ';'

    def print_result(self):
        print self.jresponse


if __name__ == '__main__':
    res = MyYandexDirectApi()
    res.get_camaning('sbx-pythonoI0dSg')
