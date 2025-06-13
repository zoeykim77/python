# (1)
# 주문이 들어올 때마다 손님의 이름과 주문 내역이 딕셔너리에 저장됩니다.
# 딕셔너리에서 ‘order’ 값만 출력하세요

order_info = {"customer": "Kim", "order": "iced americano"}

# 정답 
order_info['order']

# 내답 
order_info.get("order")
print(order_info.get("order"))

# (2)
# 배달 주문을 위해, 주소 정보를 추가로 저장해야 합니다
# 아래 딕셔너리에 'address':'Seoul, Jongno-gu'를 추가하고 전체 딕셔너리를 출력하세요.

delivery = {"customer": "Choi"}

# 정답 : 아예 새로운 key 추가 
delivery["address"]='Seoul, Jongno-gu'
print(delivery)

# (3)
# 카페 인기 메뉴의 주문 횟수를 기록한 딕셔너리입니다.
# 모든 메뉴 이름(키)만 리스트로 추출하는 코드를 작성하세요.
orders = {"latte": 21, "americano": 32, "bagel": 15}

# 정답 : 
orders.keys()
print(orders) # 기존 oders 딕셔너리로 출력 why??
print(orders.keys()) # dict_keys(['latte', 'americano', 'bagel']) 출력 
print(list(orders.keys())) # 리스트로 뽑기 

# 심화 : 가장 많이 팔린 순으로 정렬 원할시 
# 순서가 없는 딕셔너리 -> 리스트로 변환후 

order_list=list(orders.items()) #재할당 #키:값 한쌍구조의 튜플이 있는 리스트 생성 
order_list.sort(key=lambda x:-x[1]) #1번째 위치값을 내림차순으로 정렬! 
print(order_list) #왜 재할당 없이 바로 sorted 되어 나옴? 수정없이 재정렬이라???? 

# 심화 예시 : 
for menu, cnt in order_list:
    print(f'{menu}는 {cnt}개 팔렸습니다.')

for menu, cnt in enumerate(order_list):  


# (4)
# VIP 고객인지 확인하려면 'grade'라는 키가 있는지 딕셔너리에서 확인해야 합니다.
# 아래 딕셔너리에 해당 키가 있는지 True/False로 출력하는 코드를 작성하세요.
customer = {"name": "Lee", "point": 1500}


# 방법 1: #print만 해줘도 T/F로 나옴 
print('grade' in customer)

# 방법 2 : grade있나 찾고 대치가능 (직접 f 입력)
print(customer.get('grade',False))

# 내답 
customer.get("grades")
print(customer.get("grades")) # none으로 뜸, 오류 없이 

if "grades" in customer:
    print("true")
else:
    print("false")
    
    
# 만약 'grade' 키가 없다면,
# 고객의 'point' 점수를 기준으로 등급을 자동 부여하여 딕셔너리에 추가하세요.
    # - 2000점 이상: "VIP"
    # - 1000점 이상: "Gold"
    # - 500점 이상: "Silver"
    # - 500점 미만: "Bronze"
    
 # 정답 : if 문으로 ! 어떻게 새로운 key 자동생성하고 바로 넣어? 
 
if "grades" not in customer.keys():
    if customer['point'] >=2000:
        customer['grade'] = 'vip'
    elif custmoer['point'] >=1000:
        customer['grade'] ='gold'
    
print(customer)