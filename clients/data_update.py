from pymongo import MongoClient

def exec_update(zone_name, max_car):

    client = MongoClient('mongodb://test:test@3.129.66.108', 27017)
    # client = MongoClient('localhost', 27017)
    db = client.dbteamdi

    ###구현
    db.socarzone.update_one({'zone_name': zone_name},{'$set': {'max_car':max_car}})
    print("update success")

# exec_update('성균관대역 환승주차장(주차비카드제공)',"3")