fruits = ['사과','배', '감','귤',]

for fruit in fruits:
    print(fruit)


# 리스트 안에 찾고싶은 value 가 몇개 있는지 파악하는 함수

fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']


def fruit_counter(name):
    count = 0
    for fruit in fruits:
        if (fruit == name):
            count += 1
    return count

result = fruit_counter('감')
print(result)

# 사람 이름 (리스트 안의 딕셔너리)

people = [
        {'name': 'bob', 'age': 20}, 
        {'name': 'carry', 'age': 38},
        {'name': 'john', 'age': 7}
]

for name in people:
    print(name['name'])

# 이름을 받으면 나이를 가져오는 함수

def get_age(myname):
    for person in people:
        if person['name'] == myname:
            return person['age']
        return '해당하는 이름이 없습니다'


print(get_age('bob'))
print(get_age('kay'))