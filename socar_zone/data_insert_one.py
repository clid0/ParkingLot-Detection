import csv
from pymongo import MongoClient

import sys

# list1 = sys.argv
#
# if len(sys.argv) != 6:
#     print("Insufficient arguments")
#     sys.exit()
def exec1(a,b,c,d,e,f):

    client = MongoClient('mongodb://test:test@3.141.15.72', 27017)
    # client = MongoClient('localhost', 27017)
    db = client.dbteamdi

    # f = open('../zone_info.csv', 'r', encoding='utf-8')
    # rdr = csv.reader(f)
    # rdr = list(rdr)
    name = "zone_name"
    lat = "zone_lat"
    lng = "zone_lng"
    address = "zone_address"
    car = "max_car"
    limit_car = "limit_car"

    dic = {
            name: a,
            lat : b,
            lng : c,
            address : d,
            car : e,
            limit_car : f
        }

    db.socarzone.insert_one(dic)
    print('success')
    # db.socarzone.insert_one(dic)
    # for line in rdr:
    #     dic = {
    #         name: line[1],
    #         lat : line[2],
    #         lng : line[3],
    #         address :line[4],
    #         car : line[5]
    #     }
    #     db.socarzone.insert_one(dic)
    # f.close()

