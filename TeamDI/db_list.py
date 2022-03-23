from pymongo import MongoClient
client = MongoClient('mongodb://test:test@3.141.15.72', 27017)


def run(a = []):
  db = client.dbteamdi 
  ls1 = db.socarzone.find({})
  result = []
  for i in ls1:
    result.append(i["zone_name"])
  return result
