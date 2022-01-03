from pymongo import MongoClient
# import data_all, data_delete, data_update, data_insert_one
import time
import subprocess
import os.path
import gridfs

from flask import Flask, render_template, session, jsonify, request, redirect, url_for

app = Flask(__name__)
app.secret_key = "12312sdasdasd"

client = MongoClient('mongodb://test:test@3.141.15.72', 27017)
# client = MongoClient('localhost', 27017)
db = client.dbteamdi


# HTML 화면 보여주기
@app.route('/')
def home():
    if "userID" in session:
        return render_template('map.html', login =True)
    else:
        return render_template('index.html',login = False)

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/logout',methods=['GET'])
def logout():
    session.pop("userID")
    print(session)
    return jsonify({'msg': '로그아웃!'})




@app.route('/check',  methods=['POST'])
def check():
    email_receive = request.form['email_give']
    password_receive = request.form['password_give']
    doc = {
        'email': email_receive,
        'password': password_receive
    }
    a = db.clients.find_one({"email":email_receive})

    if a is not None:

        if a['email'] == email_receive and a['password'] == password_receive:
            session["userID"] = email_receive
            return redirect(url_for("map"))
        else:
            return jsonify({'msg': '패스워드 틀림!'})
    else:
        # render_template('html.html')
        return jsonify({'msg': '로그인실패!'})

    return render_template('index.html')

@app.route('/api/zones', methods=['GET'])
def all_zones():
    zones = list(db.socarzone.find({},{'_id':False}))
    # print(zones)
    return jsonify({"list" : zones})

@app.route('/openimg', methods=['POST'])
def open_img():
    name_receive = request.form['name_give']
    dic = {
        'zone_name': name_receive
    }
    zone = db.socarzone.find_one({'zone_name' : name_receive},{'_id':False})


    zone_name = zone['zone_name']
    print("zone_name",zone_name)
    print("name_receive",name_receive)
    fs = gridfs.GridFS(db)
    data = client.dbteamdi.fs.files.find_one({"zone_name":zone_name})
    if data is not None:
        print(data)
        my_id = data['_id']
        outputdata = fs.get(my_id).read()
        dir1 = './static/' + zone_name
        if os.path.isdir(dir1):
            path = "./static/"+zone_name+'/detected.jpg'
            f2 = open(path,"wb")
            f2.write(outputdata)
            f2.close()
        else:
            os.mkdir('./static/' + zone_name)
            path = "./static/" + zone_name + '/detected.jpg'
            f2 = open(path, "wb")
            f2.write(outputdata)
            f2.close()

        img_url = '../static/' + zone_name + '/detected.jpg'  # 여기가 핵심임.
        return jsonify({"img_url": img_url})
            # os.mkdir('./static/' + zone_name)
            # img_url = '../static/' + zone_name + '/detected.jpg'  # 여기가 핵심임.
            # return jsonify({"img_url": img_url})
    else:
        return jsonify({"img_url": "없습니다"})




if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

