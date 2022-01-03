from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request, redirect, url_for, session

app = Flask(__name__)

client = MongoClient('mongodb://test:test@3.141.15.72', 27017)
# client = MongoClient('localhost', 27017)
db = client.dbteamdi

app.secret_key = 'hihi'

@app.route("/")
def home():
    if "userID" in session:
        return render_template("index2.html", username = session.get("userID"),login =True)
    else:
        return render_template("index2.html")

@app.route('/map')
def map():
    return render_template('map.thml')

@app.route("/login",methods=["get"])
def login():
    _email_ = request.args.get("email")
    _password_ = request.args.get("password")
    print("sdf",_email_, _password_)

    a = db.clients.find_one({"email": _email_})
    # print('find_one')
    # print(a)
    if a is not None:
        if a['email'] == _email_ and a['password'] == _password_:
            print(_email_, _password_,a['email'])
            session["userId"] = _email_
            redirect(url_for("map"))
        else:
            redirect(url_for("map"))
    #         return jsonify({'msg': '로그인!', 'name': 'map'})
    #         # return jsonify({'msg': '로그인!'})
    #     else:
    #         return jsonify({'msg': '패스워드 틀림!'})
    # else:
    #     # render_template('html.html')
    #     return jsonify({'msg': '로그인실패!'})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)