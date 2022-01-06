from pymongo import MongoClient
import random



def exec_update(zone_name, limit_car):
    ###구현
    db.socarzone.update_one({'zone_name': zone_name},{'$set': {'limit_car':limit_car}})
    # db.users.update_one({'name': 'bobby'}, {'$set': {'age': 19}})
    print("update success")


client = MongoClient('mongodb://test:test@3.141.15.72', 27017)

db = client.dbteamdi

a = db.socarzone.find({"zone_name":'거주자우선주차구역'})


db.socarzone.update_one({'zone_address': '서울 서대문구 북가좌동 340-35'}, {'$set': {'limit_car':'30'}})
print(list(a))

