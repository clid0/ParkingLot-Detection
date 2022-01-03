from pymongo import MongoClient

def exec_delete(zone_name):

    client = MongoClient('mongodb://test:test@3.129.66.108', 27017)
    # client = MongoClient('localhost', 27017)
    db = client.dbteamdi

    ###구현
    db.socarzone.delete_one({'zone_name': zone_name})
    print("delete success")

# exec1('서울광장')