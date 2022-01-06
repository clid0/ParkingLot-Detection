import csv
from pymongo import MongoClient
client = MongoClient('mongodb://test:test@3.141.15.72', 27017)


# ### socarzone insert datas
# db = client.dbteamdi
# f = open('zone_info.csv', 'r', encoding='utf-8')
# rdr = csv.reader(f)
# rdr = list(rdr)
# name = rdr[0][1]
# lat = rdr[0][2]
# lng = rdr[0][3]
# address = rdr[0][4]
# car = rdr[0][5]
#
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
#
# ###
db = client.dbteamdi

dic = {
    "email": "abcd@naver.com",
    "password": "123",
    "name": "홍길동"
}
db.clients.insert_one(dic)
# print("success")