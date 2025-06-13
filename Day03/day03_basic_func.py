# 함수 기초 (문제)
# 함수 사용전 (일일히 넣어서 값구함)
number1 = 5
number2 = 10

# 둘 중 무엇이 큰지 비교 
if number1 > number2:
    answer = number1 
else:
    answer = number2 
print(answer)

#answer 초기화(초기값) 안써도 됨. 조건 어디든 걸리니까. 

number3=7
number4=4

# 뭐가 큰지 비교 
# 동일절차반복필요

# 함수사용 후
# 1)함수 정의(define)
# 함수라고 하는 박스를 만든다. 

def get_bigger(num1, num2):
    if num1>num2:
        return num1 
    else:
        return num2

# def 함수정의는 박스만 만든것이라, "아무일도 일어나지 않는다"
# 호출(call) 실행해줘야 한다. 

# 2)함수 호출(call)
# 함수를 불러와서 사용하는 것을 의미. 입력값이 필요하다.
# 매개변수 : input 함수에 전달되는 입력을 저장하는 곳  
# 인자 : 함수 호출시 함수에 전달되는 값 
# 반환값 : output, 함수거친후 나오는 값. return 뒤의 값 
print(get_bigger(number1,number2))
print(get_bigger(number3,number4))
