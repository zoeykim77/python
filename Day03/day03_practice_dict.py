# 딕셔너리 실습
# 1.생성 # 딕셔너리 {} 중괄호로 생성, key는 불변한 문자열로! 
# 정보를 담은 user 딕셔너리 생성
# name, age(한국나이), city, is_maele 정보 담기

user ={'name': '김경현', 
        'age': 37,           #int형으로 value생성(key는 불변한문자열이지만) 
        'city' :'seoul'      #value에 텍스트니 '' 필요 
        'is_male': False}

print(user)

# 2. 수정 # [] 대괄호는 key값 기준 인덱스해 값 찾기 때문. 
# 실수로 age값 한국나이로 적음.
# 만나이 기준으로 해줘 
# 재할당 및 복합연산 

# 방법 1) 재할당 
user['age'] = 36 # value값 재할당 
print(user)

# 방법 2) 복합연산 
user['age']-=1 

# 3. 추가 #딕셔너리는 key 기준으로 value 저장하기에, 그대로 추가해줘도 됨. 리스트는순서. 
# 운전면허보유여부를 나타내는 license에 정보담기

user['license'] = True 
print(user)

# 4. 삭제
# 우리 모두 city는 서울로 동일함
# city 정보 삭제해주세요 

user.pop('city')
print(user)

# 길이확인가능 
print(len(user)) #길이가 4인 딕셔너리임, class dict. 