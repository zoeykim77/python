# 멤버십 연산자 
# in, not in
# 특정한 값이 "컨테이너 자료형"에 포함되어 있는지 검사 하는 연산
# 있으면 T, 없으면 F 

#리스트와 멤버십 연산자 
numbers = [1,2,3,4,5]

for num in numbers:
    if num == 1:
        print('1을 찾았습니다.')
        break 

# for문 보다 간단히 표기 
print(2 in numbers) 
print(100 in numbers)
print(100 not in numbers) # n이 리스트안에 없으면 T (반전)


#딕셔너리와 멤버십 연산자 
colors = {'red':'빨강',
          'blue':'파랑',
          'yellow':'노랑'}
print(colors)

# key 모음에 포함될 때만 True 
print('빨강' in colors) #오류! key모음에 포함될때만 T로 인식, value값으로 검색함 
print('red' in colors) # True로 뜸! key값으로 검색했기에  

# value 값 검색하고 싶을땐 메소드 
print(colors.vlaues('파랑')) #메소드로 확인시, 밸류값만 나열 #메소드는 소괄호()표기! 
