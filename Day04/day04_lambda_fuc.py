# 익명함수 : 이름 없고, 일회성 (이름 붙일만큼 중요치x)
# lambda 
# 매개변수 : 표현식

# 기존 방식(함수)
def add(x,y):
    return x+y
result = add(1,4)
print(result) #5  

# 익명함수 이용방식 
# 간단한 함수는 함수로 선언,호출 불요. 더 간단하게! 
# 정렬에 key로 쓰이거나, 어떤 자료 한번에 바꿀때 정도로만 쓰임. (복잡연산엔x)

lambda x,y:x+y
result = (lambda x,y:x+y)(10,2)
print(result)

# lambda 함수로 정렬하기 + sorted함수
number = [1,5,3,5,7]
sorted(number, key=lambd x:-x)
number_new = sorted(number, key=lambd x:-x)
print(number_new) #number의 요소를 -로 바꾸고, 오름차순 정리한 값 나옴 
print(sorted(number, reverse=True) #sorted함수 내림차순 정리 

# 리스트의 형식 : 리스트속 튜플의 key값 기준 정렬 
example = [(1,2), (2,3),(3,4)]]
new_example = sorted (example, key=lambda x:x[1]) #리스트 내 튜플(,)의 뒤값(위치) 
print(new_example) 

# 딕셔너리 형식 : key 기준 정렬 or value 기준 정렬 가능 

# 예시) 떡잎마을 반장선거, 수지만 뽑기

result_lst = list(result.items())
print(result_lst)
result_lst.sort(key=lambda x:-x[1]) 
print(result_lst) # 리스트 중 (수지: ) 쌍이 가장 처음 나열. 
print(result_lst[0][0]) #그중 제일 처음 value값으로 검색시 수지 나옴. 
print(result)
print('수지가 반장이 되었습니다')