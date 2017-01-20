# coding=utf-8
import urllib
import json
import ssl


def cities():
    context = ssl._create_unverified_context()
    url = 'http://www.pecom.ru/ru/calc/towns.php'
    req = urllib.urlopen(url, context=context)
    res = json.load(req)
    print res


def light_defelop():
    context = ssl._create_unverified_context()
    url = 'http://pecom.ru/api/pallet.php?'
    data = {
        'from': 446,  # ID города отправки. Доступна только Москва (446).
        'to': 448,  # ID города получателя
        'type': 3,  # Тип паллеты: евро-стандарт (1), финская (2), американская (3)
        'amount': 2  # Количество паллет в штуках
    }

    req = urllib.urlopen(url + urllib.urlencode(data), context=context)
    res = json.load(req)
    print res


def hard_develop():
    context = ssl._create_unverified_context()
    url = 'http://calc.pecom.ru/bitrix/components/pecom/calc/ajax.php?'
    length = 0.5
    width = 0.3
    height = 0.7
    volume = 0.1
    mass = 60
    oversize = 1
    ju = 1

    data = {
        'take[town]': -446,
        'deliver[town]': -463,
    }
    size = '&places%5B0%5D%5B%5D={}' \
           '&places%5B0%5D%5B%5D={}' \
           '&places%5B0%5D%5B%5D={}' \
           '&places%5B0%5D%5B%5D={}' \
           '&places%5B0%5D%5B%5D={}' \
           '&places%5B0%5D%5B%5D={}' \
           '&places%5B0%5D%5B%5D={}&'.format(length, width, height, volume, mass, oversize, ju)
    req = urllib.urlopen(url + size + urllib.urlencode(data), context=context)
    res = json.load(req)
    print res['auto'], res['ADD'], res['periods_days']



hard_develop()

# url = 'http://calc.pecom.ru/bitrix/components/pecom/calc/ajax.php'
# print url + '?' + urllib.urlencode(url, doseq=1)

"""
    data = {
        'take[town]': -60573,
        'take[tent]': 0,
        'take[gidro]': 0,
        'take[manip ]': 0,
        'take[speed]': 0,
        'take[moscow]': 0,
        'deliver[town] ': -404524,
        'deliver[tent]': 0,
        'deliver[gidro]': 0,
        'deliver[manip ]': 0,
        'deliver[speed]': 0,
        'deliver[moscow]': 0,
        'milage_from': 0,
        'milage_to': 0,
        'plombir': 0,
        'strah': 0,
        'ashan': 0,
        'night': 0,
        'pal': 0,
        'pallets': 0,
        'ju': 'false',
        'need_take ': 0,
        'need_deliv': 0,
        'max_dimension': 1,
        'total_volume': 1,
        'total_weight': 1,
    }

"""