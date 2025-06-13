# 로직 실전문제풀이 
# max, min

numbers = [190,49, 3,-1, -99, 2, 490]
max_value = max(numbers)
print(max_value)

min_value = min(numbers)
print(min_value)

# numbers를 반복하며, 각 요소와 max value 비교 
# 비교한 게 더 큰 값을 다시 max value에 할당 

numbers = [190,49, 3,-1, -99, 2, 490]
max_value = -999 # 충분이 작은 최대값 

for num in numbers:
    print (num)
    if max_value < num: 
       max_value = num #전체순회하며, num이 max보다 더 크면 max값으로 대체, 재할당 
    else:
        pass 
      

numbers = [190,49, 3,-1, -99, 2, 490]
min_value = 999 # 충분이 큰 최소값

for num in numbers:  
    # print(min_value) 
    # 하나씩 순회 잘 실행되나 확인하기 위해 중간마다 print(min_value) 체크가능..
    if min_value > num:
        min_value= num
    else:
        pass 
    
print(min_value) #최소값만 나옴 