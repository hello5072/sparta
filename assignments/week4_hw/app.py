from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/order', methods=['GET'])
def listing():
    all_articles = list(db.week4shopping.find({},{"_id":0}))
    # 1. 모든 document 찾기 & _id 값은 출력에서 제외하기
    # 2. articles라는 키 값으로 영화정보 내려주기
    return jsonify({'result':'success', 'week4shopping':all_articles})

## API 역할을 하는 부분
@app.route('/order', methods=['POST'])
def saving():
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    contact_receive = request.form['contact_give']

    # headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    # data = requests.get(url_receive,headers=headers)
    # soup = BeautifulSoup(data.text, 'html.parser')

    # image = soup.select_one('meta[property="og:image"]')['content']
    # title = soup.select_one('meta[property="og:title"]')['content']
    # desc = soup.select_one('meta[property="og:description"]')['content']

    doc = {
        'name': name_receive,
        'count': count_receive,
        'address': address_receive,
        'contact': contact_receive
    }

    db.week4shopping.insert_one(doc)

    return jsonify({'result': 'success', 'msg':'저장이 완료되었습니다'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)