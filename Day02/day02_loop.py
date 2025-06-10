# for 반복문
# 반복회수가 정해져 있을때, 사용한다.

#기본사용법
# for 변수 in 컨테이너: (콜론필요)
    #반복코드(들여쓰기필요)
for i in range(10): #in 다음엔 순회가능한 자료(리스트등) 올수 있다. 
    print(i)
    
#1.리스트 순회하기

names = ['ken','jun','justin']
for name in names:
    print(f'안녕하세요, {name}님!')

print(name) #맨마지막 justin 뜸 

#2. 문자열 순회하기
word = 'python' #문자열은 input함수에서만 자동str, 별도 '' 표기하기
for character in word: #word내 파이썬을 캐릭터에 할당
    print(character) #p,y,t 순으로 끝까지 순회한다. 
print(len(word)) #len함수는 순회 길이. 6회 

#3.조건문 함께 사용
numbers = list (range(1,11)) #1-10까지 직접 입력말고, 함수로 간단케!
print(numbers)

for number in numbers:
    if number % 2 == 0: #짝수인 경우에만
        print(number) #출력 

#range 이용한 정수목록 (위와 동일한 값!) 
#특정 횟수만큼, 특정코드 반복시 활용한다. 
#for_in range(n) 언더바,i는 큰 의미 없다. 알아서 잘 작성. 

for number in range(1,11):
    if number % 2 == 0:
        print(number)
        
#for문 간단실습문제
#for문, range 활용해 1~10 더한 값 55출력하기

answer = 0

for i in range(1,11):
    #range를 순회하며, i에 순서대로 할당
    print(i) 
    answer = answer + i # 복합연산자 += 을 통해 재할당 가능! 
    print(f'answer의 변화 : {answer}')

#코드작성 
print(answer) #55 

#조건에 따라 합산도 가능 
answer = 0
for i in range(1,11):
    if i % 2 == 0 : #짝수인케이스만 
        answer += i 
        print(f'answer의 변화:{answer}')

print(answer)

#조건문+반복문 같이 쓰이는 경우 많다. 

#인덱스의 순회, 필터링 
#len() range() for문 활용???