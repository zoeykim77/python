# 내장함수
numbers = [1,4,10,33,-9]
# 내장함수 len, max, min, sum, abs () 가능!
# 예시) print(len(numbers))

# 순서가 있는 컨테이너
# 순서가 있다는 것이 정렬되었다는 것은 아니다! (정렬이란? )

# 내장함수 sort
sorted() #sorted 함수는, 순서있는 자료형 원소를 정렬후 리스트로 반환(오름차순)
numbers_new = sorted(numbers)
#sorted 함수 적용한 새변수, 오름차순 정렬된 list 반환, 이때 id 달라짐 


# 내장함수 map 
number_str=list(map(str, numbers)) #map만 하면 위치만 찍음? list화 필요 
print(number_str) #각 넘버링 요소들을 리스트화, 문자열화 '' 

# 매개 변수 and 반환값
# 1) 매개변수, 반환값 있는경우
# 2) 매개변수, 반환값 x 
.append 는 리스트 값 추가하지만 반환값없다.
# 3) 매개변수 x
입력없이 매번 정해진 처리만 하는 것. 함수 밖에서 끌어와서 쓸때
# 4) 매개x 반환x 
항상 정해진 처리만 하는 것 