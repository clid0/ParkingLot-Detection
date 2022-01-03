from flask import Flask, request, render_template, jsonify
import gridfs

app = Flask(__name__)


from pymongo import MongoClient

client2 = MongoClient('localhost', 27017)
db2 = client2.cityclone

client = MongoClient('mongodb://test:test@3.141.15.72', 27017)
# client = MongoClient('localhost', 27017)
db = client.dbteamdi

### detect.py 에 삽입할 코드
### 이 파일이 데이터 베이스에 들어가야함. -> 여기의 사진이 detect된 사진임
f = open("./static/teamdi_logo.png","rb")
fs = gridfs.GridFS(db)
fs.put(f, filename = 'name')

### app.py에 삽입될 코드
### 이걸 app.py에 삽입하고 static에서 꺼낼 수 있도록 하자


### 해야 할 일: 몽고 db데이터 베이스 손보기
# data = client2.cityclone.fs.files.find_one({"filename":'name'})
#
# print(data)
# my_id = data['_id']
# outputdata = fs.get(my_id).read()
# f2 = open("./static2/hi4.jpg","wb")
#
# # output = open('./statics2/' + 'back.jpeg', 'wb')
# f2.write(outputdata)
# f2.close()


data = client.dbteamdi.fs.files.find_one({"zone_name":'아마노 감리신학대학교점'})

print(data)
my_id = data['_id']
outputdata = fs.get(my_id).read()
f2 = open("./static2/hi4.jpg","wb")

# output = open('./statics2/' + 'back.jpeg', 'wb')
f2.write(outputdata)
f2.close()

### 삭제 코드
# client2.cityclone.fs.files.delete_one({"filename":'name'})
