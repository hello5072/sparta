from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

## 코딩 할 준비 ##

target_movie = db.movies.find_one({'title':'매트릭스'})
# 매트릭스 평점 가져오기
# print(target_movie['star'])

# 매트릭스의 평점과 같은 영화 제목들을 가져오기
target_star = target_movie['star']

# movies = list(db.movies.find({'star':target_star}))

# for movie in movies:
#     print(movie['title'])

# 매트릭스와 같은 평점을 가진 영화들 평점 다 0 으로 바꾸기


db.movies.update_many({'star': target_star},{ '$set':{'star':0} })
