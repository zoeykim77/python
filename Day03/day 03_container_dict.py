# 순서가 없는 컨테이너 

# 딕셔너리 : {} 중괄호로 표기 / ,콤파요소나열 / key : value 콜론 연결
# 0개 이상의 순서없는 요소들 항목 저장 key:value 구조, 1:1 맵핑 
# key 를 기준으로 값 저장됨. 유일해야함. 가장 마지막 요소로 표현

user = {'name':'jun', #name key값 두번쓰면, 마지막 이름으로 적용 
        'age': 20,
        'license':True}
print(user)

# 딕셔너리 특징 1 : 순서가 없다.
# key:value 쌍으로 이루어져 있다.

# key는 유일해야하기에 바뀔 수 없다. 
# -> 바뀔 수 없는 자료형 써야 한다(immutable)
# -> 숫자형, 불리언TF, 튜플, 문자열 등 (보통문자열 많이옴)
# value는 자료형 구분없이 사용가능 

# 접근
# key를 기준으로 인덱싱하여 -> value에 접근한다.
print(user['age']) #대괄호 인덱싱 [] 내 key로 인덱싱, value값 불러옴 

# 딕셔너리 특징 2: 가변자료형(mutable)
# 값을 변경해도 똑같은 주소 (id) 가진다. 

# 수정 
user['age'] = 30 #20대신 30으로 재할당 가능, id 동일 
print(user) 
print(id(user)) 

# 추가 (리스트는 범위 밖 인덱싱 추가 불가??, 딕셔너리는 가능. key를 기준 맵핑하니)
# 할당으로 새로운 key-value 를 추가할 수 있다.  
# 딕셔너리 메소드로 새 값 할당 가능 (반복문 활용시)

user['is_male'] = True 

# 삭제
user.pop('license') 
# 리스트는 순서 o, pop()공백인식해 마지막 요소를 삭제. 
# 딕셔너리는 순서 x, pop()공백은 뭘 삭제할지 모름. 삭제할 1개이상 key값 설정 필요 

# 딕셔너리 메서드
# key 만 확인하기 
print(user.keys()) #딕셔너리 내 key값만 나열 
print(list(user.keys())) #딕셔너리 내 key를 리스트 형식으로 볼 수 있음. 

# value 만 확인하기
print(user.values()) #각 key에 해당하는 값들만 나열 

# key:value 한번에 보기(매핑해보기), value 값만 뜨면 리스트처럼 값이 무엇을 뜻하는 지 모름 
# key:value 역할을 무시하고, (쌍 제거하고) 튜플로 반환 
print(user.items()) #키별로 값 쌍으로 나옴 
user_list = list(user.item()) #튜플로 바꾸고(순서가 없는 dic을 list화니까 튜플)
print(user_list[0])
print(user_list[0][0]) # 첫번째 요소만 가져온다. ??? #리스트 안에 리스트 있는경우?