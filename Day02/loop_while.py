# 반복문 - while 
# 반복횟수 정해져 있지 않다.
# while True: #현재는 무한히 반복
#    print('영원히 반복') 

# while 조건:
    # 반복되는 코드 

numbers = [1,2,3,4,5]
i=0 # 시작전,i로 꼭 할당필요하다 

while i < len(numbers):
    print(numbers[i]) #무한반복중? 무엇까지?? 
    i += 1 # 조건을 변화시킬 수 있는 식이 꼭 필요하다. (아니면 무한반복됨. 제한걸어줌)
    
# while 문으로 1부터 10까지 출력하기

for i in range(1,11):
    print(i)

i = 1    # while문은 i값 초기설정 필요 
while i < 11: # 증감식에서 꼭! 조건 변화시킬 수 있어야 한다. 
              # or 1-10 or 111 나열 무한반복됨?? while조건문 아래 코드탭에 조건문 한정 
    print(i)
    i += 1 # 중요한 증감식 부분! ??? 계속 합해지는거 아님? 
    

# while문으로부터 1부터 10까지 더한값 55 출력하기 

n = 1 
answer = 0 #초기값 설정 

while n <= 10:
    answer += n #누적필요, 재할당! 복합연산가능(기본식)
    n += 1 # 조건에 대한 증감식 (제한용 증감식)

#while 아래 기본식,증감식 바뀌면 값 달라짐 

print(answer)  
