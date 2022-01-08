import gridfs

from pymongo import MongoClient
client = MongoClient('mongodb://test:test@3.141.15.72', 27017)
import sys
import os

db = client.dbteamdi

ls = list(db.socarzone.find({}))
for i in ls:
  name = i['zone_name']
  # path = '/content/drive/MyDrive/socar_zones'
  os.makedirs(name,exist_ok=True)

# name = 'hi'
# path = '/content/drive/MyDrive/socar_zones/'
# os.mkdir(name)