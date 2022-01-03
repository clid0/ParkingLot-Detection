from pymongo import MongoClient
import random



def exec_update(zone_name, limit_car):
    ###구현
    db.socarzone.update_one({'zone_name': zone_name},{'$set': {'limit_car':limit_car}})
    # db.users.update_one({'name': 'bobby'}, {'$set': {'age': 19}})
    print("update success")


client = MongoClient('mongodb://test:test@3.141.15.72', 27017)
# client = MongoClient('localhost', 27017)
db = client.dbteamdi
ls1 = list(db.socarzone.find({},{'_id':False}))
for i in ls1:
    x = random.randint(15,30)
    exec_update(i['zone_name'],str(x))