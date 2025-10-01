# 다음과 같은 api 데이터가 있을 때, 모든 유저들의 이름을 모아보시오.
users = {
    'total_user': 3,
    'information': [
        {'name': 'alex', 'age': 3, 'license': True},
        {'name': 'june', 'age': 7, 'license': False},
        {'name': 'peter', 'age': 4, 'license': False}
    ]
}

names = []

# 로직 작성

infos = users['information']
print(infos)

for n in infos['name']: # if 문에 n 넣으면, n의 정의 필요! 
         names.appened(infos['name'])

print(names)  # ['alex', 'june', 'peter']
