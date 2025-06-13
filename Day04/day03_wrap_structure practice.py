# 문제 (구조화)
users = {
    'total_user': 3,
    'information': [
            {'name': 'alex', 'age':3, 'license':True},
            {'name': 'june', 'age':7, 'license':False},
            {'name': 'peter', 'age':4, 'license':False}]}


# 첫째, 구조에 대한 이해 필요 
# 딕셔너리 > 값 : 리스트 > 값 : 딕셔너리 
# users = 딕셔너리, user.keys() 
# 전체 구조에 대한 이해를 하는 지, 딕셔너린 키로 값 불러온다, 리스트는 인덱스로

# 구조확인하기 
print(type(users)) # 딕셔너리
print(users.keys()) 
prints(users['total_user']) # int
print(type(users['information'])) #리스트 

# 사람들 정보만 뽑아보기 
infos = users ['information'] # 큰 구조에서 정보만 뽑기, 더 쉽게 만들어두기  
print(infos[0]) # 그 안에서 또 이름만 뽑기 

# 1. 라이센스가 있는 인원수 세기 

cnt=0 #초기값 설정

for info in infos: #기존 infos로 편하게 쓸 구조만 빼둠 
    if info['licnese']: #license는 불린형이니 그냥 써주기만 해도됨 
        cnt +=1 
        
print(f'라이센스가 있는 인원: {cnt}명')


# 오답
for lic in users:
    if lic == users['license']:
        answer += 1
print(answer)

# 정답 
answer = 0 #초기값 설정 

for user in users['information']:
    if user['license']:  
        answer += 1
        
print(answer)

# 2. 모든 사람의 나이 평균 구하기 

print(users['total_users']) #3
age_sum = 0

# 방법 1 : 숫자형 변수와 불린 
age_sum = 0 #초기값 설정 

for info in users['information']: # info중의 key값으로 value 값 받아옴 
    age_sum += info['age']
ave_age = age_sum/users['total_user'] 
print(f'나이의 평균은 {round(av_age,2)}살입니다.') #round로 반올림, 2의 자리수까지만 

# 방법 2 : 리스트와 내장함수 활용 
age_list = [] #빈 리스트 생성후, 추가해줌 

for info in infos:
    age_list.append(info['age'])

print(sum(age_list)/len(age_list)) #total_users로 불러오지말고, len 활용 
    
    
# 오답 (내장함수average 없음)
for average in users:
  print(sum(user['age'])/total_users) 
    
    
#3. 라이센스가 없는 사람들의 이름 모으기 
name_list = [] # 빈 리스트 생성 

for info in infos:
    if not in info['license']: 
    #or if info ['license'] == False:
    name_list.append(info['name'])

print(name_list)

# 오답 
non_list = list['name']

for non_lic in users:
    if non_lic['information']['license'] != False:
        print(non_list)


# 추가문제 : 딕셔너리 내 요소에 값 변경, 더하기 (구조파악시, 여러수정 용이)

users['total_user'] += 1
users['information'].append({'name': 'ken', 'age':10, 'license':False})




