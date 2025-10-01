# Q. <별 찍기> 문제 
# 자연수 N 입력받아, N줄까지 "별을 출력하는" 함수를 만들기
# 첫번쨰 줄은 별이 1개, N번째 줄은 N개의 별이 찍혀애 한다
# ex) 만약 N이 3이면? 

n = 3
'*'*1
'*'*2
'*'*3


# 문자열인 *이 반복된다. (곱셈으로 나타내기)
'*'*i 

for i in range(1,n+1): # 정수모음인 range이용(0~n-1), 1부터 찍어주기 
    print('*'*i) #str *는 그냥 '' 만 해줘도 인식! str 변환 불요 
    
# *의 갯수는 이해, 왜 줄이 각각나옴?  
    
# 함수선언 (define)
# 매개변수 유, 반환값 무 

def print_star(n):
    for i in range(1, n+1):
        print('*'*i)

# 호출 (call)
# 올바른 호출법 
n = int(input('정수를 입력해 주세요.:'))
print_star(n)


# 잘못된 케이스 1 : 입력받아야 하는데 입력 받지 못함 
print_star() # () 오류뜸, input/ 매개변수를 아예 안넣은 경우 

# 잘못된 케이스 2 : 반환되는 값이 없는데, 값을 달라고? 
print(print_star(n)) # none 오류 뜸. 
# 반환되는 값이 없는데, 달라고? 
# 파이썬에서 자체적 답 없다 "none" 으로 출력 

# 오답 
n = int(input())


def print_star(n):
    if n:
        n = 
        print(f{*})
    

print_star(n)