import gridfs
# import csv
from pymongo import MongoClient
client = MongoClient('mongodb://test:test@3.141.15.72', 27017)
import sys


# zone_name1 = sys.argv[1]+' '+sys.argv[2]
zone_name1 = sys.argv[1]
# img_path = sys.argv[2]
db = client.dbteamdi 
a = db.socarzone.find_one({"zone_name":zone_name1})
print(a)
if client.dbteamdi.fs.files.find_one({"zone_name":a['zone_name']}):
  client.dbteamdi.fs.files.delete_one({"zone_name":a['zone_name']})

path = '/content/drive/MyDrive/result/'+a["zone_name"]+'/detected.jpg'
f = open(path,'rb')
fs = gridfs.GridFS(db)
fs.put(f, zone_name=zone_name1)
