# 절대값을 반환하는 함수
num = -100
answer = abs(num) #absoltue 내장함수, 절대값 = 양수로 반환
print(answer)

# 1. 사용자 정의함수로 절대값 반환하는 나만의 함수 만들기 
# abs_func 이라는 함수 만들기 
# 선언,정의 (define)

def abs_func(number):
    if number > 0 :
        return number #양수면 그대로 출력 
    else: 
        return number*-1 #산술연산, 양수화   

print(abs_func(-1)) #절대값 처리 -> 1이 나옴(-1라는 인자 넣었을때 결과값줘) 
# 호출해줘야 나오니까! 
# 이렇게도 표현가능 
answer = abs_func(-1) 
print(answer)


# 오답 
def abs_func(-1):# 정수넣음 안됨-> 함수만들땐'매개변수'를 넣어야? 인자는 호출때! 
    pass # 오류무시용, 아님 터미널에서 안넘어감 
    

#2. 두 수의 차 절대값 만들기
# A와 B 정수 입력받아 두 수의 차의 절대값 반환하는 함수
# abs_diff 를 만들기 
# 선언(define)

def abs_diff(a,b):
    c= a - b 
    if c>0:
        return c 
    else c<0:
        return -1*c 

# 호출(call)
# 7과 -3을 받았다면 10 출력해야 한다. 즉 인자 7, -

answer = abs_diff(7,-3) # 혹은 바로 print(abs_diff(7,-3)으로 확인해도 됨)
print(answer)

    


    