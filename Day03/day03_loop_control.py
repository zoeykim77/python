# 반복문 제어 
# break
numbers = [1,2,3,4,5]
print(len(numbers)) #5가 뜸, 길이가 5인 리스트 

for n in numbers: # 전체 모두 실행. 즉 리스트 내 1-5 모두 실행. 반복. 요소 세로로 나열. 
    print(n)
    if n == 3: #조건설정 : 요소값중 3을 만나면, 
        print('반복을 종료합니다.')
        break #조건제어 : 3만나면 이후 요소는 반복종료되고 순회중단. 
    
# else 
# for/while 반복문이 break 에 의해 종료되지 않았을때, else문 내부 코드블럭 실행.

for number in numbers:
    if number == 30:
        print('3을 찾았습니다')
        break
    else: 
        print('30을 찾지 못했습니다.') #else 없이 쓰면 30을 찾던, 못했던 상관없이 출력됨. 
#타겟(3) 설정시, 리스트 내 요소 3이 있는 리스트라 else문 안나올 것임. 
#break 활용, 타겟(3)을 30으로(리스트 내 요소 밖의 범위) 설정시, else문 나옴 

# continue 
# 조건문 내 조건만족시, 나머지 코드 건너 뛰고 다음반복으로 넘어감 (건너뛰고 다음)
# 필터링에 씀 

number = 0
while number <= 5:
    number += 1
    if number % 2 == 0: # 짝수인 경우만, 
        continue #건너뛰어 
    print (number) #짝수 아닌경우만 출력. 즉 리스트 내 홀수만 출력 
    

# pass
# def solution(number):???????
#   pass 
# 오류를 패스한다 

numbers = [1,2,3,4,5]
for number in numbers:
    print(number)
    if number == 3: #에러 발생
        pass #오류 회피 