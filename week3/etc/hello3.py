# from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
# client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
# db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

# # db.users.insert_one({'name':'bobby','age':21})
# # db.users.insert_one({'name':'kay','age':27})
# # db.users.insert_one({'name':'john','age':30})

# # 정보 추가
# doc 이라는 임의의 변수에 딕셔너리 형식으로 값을 주고, doc을 db 에 넣는 코드
# # doc = {'name':'bob', 'age':24}
# # db.users.insert_one(doc)

# # 정보 열람
# # user = db.users.find_one({'name':'bob'},{'_id':0})
# # print(user)

# # 모든 정보 열람
# # all_users = list(db.users.find({},{'_id':0}))
# # for user in all_users:
# #     print(user)

# # 정보 수정 
# db.users.update_one({'name':'bobby'},{'$set':{'age':19}})


from pymongo import MongoClient          
client = MongoClient('localhost', 27017)  
db = client.dbsparta                      

import requests
from bs4 import BeautifulSoup


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)


soup = BeautifulSoup(data.text, 'html.parser')


movies = soup.select('#old_content > table > tbody > tr')


for movie in movies:
    
    a_tag = movie.select_one('td.title > div > a')
    if a_tag is not None:
        rank = movie.select_one('td:nth-child(1) > img')['alt'] 
        title = a_tag.text                                      
        star = movie.select_one('td.point').text                
        
        doc = {
            'title': title,
            'rank':rank,
            'star': star
        }
        db.movies.insert_one(doc)