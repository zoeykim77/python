# 예외처리 
# try : 일단 해봐!
# except : 을 제외하고 !

# 예외 처리 하지 않았을 때,
# 에러가 발생하면, 무조건 프로그램 종료 

n = int(input('숫자를 입력해주세요!'))
answer = 10/n
print(answer)

# input에 '십'이라고 넣거나 '0' 넣으면 에러메세지뜸. 


# 예외 처리 했을 경우 
# 프로그램이 정상종료 되도록 처리할 수 있다. 
try:
    n = int(input('숫자를 입력해주세요!'))
    answer = 10/n
except Exception as e:
    print(f'에러 발생: {e}')
else:
    print(answer) #에러 발생하지 않을 경우 동작도 지정필요!
    

# 예외 종류들 파악 가능한 정도만! 