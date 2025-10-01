# 함수
# 내장함수 

# 사용자 정의 함수
 
# 함수 선언(define) : 단순히 함수를 만들었을 뿐 
# def 공백 함수명 (매개변수)
# 들여쓰기 + 코드(동작)

def abs_func(i):  #i=매개변수, 매개변수명은 임의로 지어준다. 
    if i < 0:
        answer = -1*i 
    else:
        answer = i 
    return answer #answer=반환값, return으로 반환되면 다시 돌아갈 수없다?

# 함수 호출(call) : 만들어둔 함수명을 불러 쓴다. 
answer=abs_fun(-1) # -1=인자, i에 -1을 전달해줘서 함수내에서 사용하도록 함 
print(answer)
print(i) #매개변수는 함수바깥에서 확인못한다. 인자로 확인해야함. 



# Q.사용자 정의 함수로 내장함수 len 구현하기 
# len_func-> 길이를 확인할 수 있는 함수 만들기 (내장함수 쓰지말고)

numbers=[1,2,3,4,5]
answer=len(numbers) #5, len 성질은 size 를 뜻함. 


def len_func(container): # 길이값 len는 여러값이 존재하는 컨테이너속 요소길이수 
#    여러개 값이 존재하는 입력
    size = 0 # 세기 위한 변수 생성 
    for n in container: # 컨테이너 자료기에, 순회가능 for 문 
        size+=1 
    return size #return값엔 = 안붙인다./ return 위치 중요!(탭!)

# 호출(call)
answer = len_func(numbers) # answer를 새변수로 할당, 함수에 인자 넣을때마다 답보여주게! 
print(answer)

#나는 size =0 변수를 def 위에 생성, 
#나는 호출안함 

