# 리스트 메서드

numbers = [10,20,30,40,50]
print(numbers)

# 1) append 추가 
# 가장 마지막 위치에 새로운 원소 딱 하나만 추가함 
numbers.append(60)
print(numbers)

# 1-2) 여러개 추가
numbers.append(10,20,30,40) #여러개 안됨 
numbers.append([10,20,30,40]) #리스트 자체가 아예 마지막 요소자리에 추가

# 여러개 추가하고프면?
# 다른 메서드 사용 -> 가변자료형 
# extend 메소드는 list의 가변자료
number.extend([10,20,30,40]) #마지막에 리스트가 아닌 요소로 각각 추가됨! #id,같음 
numbers = numbers + [10,20,30,40] #id 다름, 새리스트 

# 2) pop 삭제 - 인덱스, 위치를 기준으로 삭제해줌 
numbers.pop(index) # 위치 조회해 삭제 

deleted_value =numbers.pop(1)
print(deleted_value) # 뭘 삭제했는지 보여줌?  

# 3) Insert 삽입
numbers.insert(3,1000) # 3번째 자리에 1000을 추가로 끼워넣어줌! 

# 4) extend, 마지막에 붙여줌 
# 객체를 바꿈 id 변경

# 특정한 원소 기준 
# 5) remove 삭제 - 원소 값을 기준으로 삭제 
numbers.remove(10) # 리스트 내 10이 여러개면, 하나만 삭제(제일 먼저있는 10만)

# 6) count 갯수세기 - 특정 원소 기준 값을 센다.
# 값을 기준으로 몇개 인지 세기에 '리스트'를 바꾸지 않는다. 
# 만약 없는 값 검색시, 0으로 나옴 

cnt=numbers.count(1000)
print(cnt) # 1, 1000이 1개라고 뜸 

# 7) index 위치찾기 - 원소값 기준으로 위치 찾을 수있다!
# 같은 값 여러개면, 딱 하나만 뜸. 먼저 나오는 위치 
idx = numbers.index(1000)
print(idx) #2, 리스트내 위치 
print(numbers[idx]) #거꾸로도 해보기, 인덱스로 검색시 1000나오는지 

# 8) sort 정렬하기 
# 내장함수 sorted : 정렬하여 새로운 리스트를 반환한다.  
# 메소드 sort() : 기존의 리스트를 정렬한다. 
# 오름차순, 알파베티컬, 역정렬 reverse=True, key 중심 정렬가능, 

numbers.sort(key=lambda x:-x) #키 값 기준 역정렬 
numbers.sort(key=lambda x:x%3) # 연산도 가능 

# 9) reverse 순서 뒤집기
numbers[::-1] 동일함, 그러나 더 파이써닉함! *추천  
numers.reverse 

