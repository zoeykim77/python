#1일차 복습
#변수 = 상자 (사실은 상자아니지만)
#할당 연산자 = 을 통해 변수를 할당함 
name = 'alex' #이제부터 name 이라는 변수를 부르면, alex가 튀어나온다! 

print('alex')
print(name)
#변수는 사용자가 사용하기 편하라고 만든다.
variable1 = 10 #의미없는 변수

age = 10
money = 30 #변수명을 설정할때에는 의미를 담아야 한다.(모든건 의미.숫자든.현상이든)

print(f'안녕하세요, {age}살의 {name}님! 오늘도 화이팅!')

#재할당 #컨테이너 이후 공부시 다시 참고 
name = 'jun' #가장 마지막에 할당한 값이 들어있게 된다. 

###자료형
###자료형이란? 데이터의 특성 
print('===자료형===')
name = 'alex'
age = 20
money = 30
is_male = True

#1.숫자
print(type(age)) #int : 정수형 (0,1,-1)
print(type(money)) #float : 실수형 (소수점이 있는 모든 숫자)

#2.문자
#"", ''를 통해 글자들의 모음을 만든다.
#쌍따옴표, 따옴표 내 들어있는 모든 것이 문자열이 된다. 
#비어있는 문자열도 문자열 ->""
#공백이 있는 문자열도 문자열 -> " "
print(type(name)) #str : 문자열 
print('')
print(" ") # 컨테이너공부시 다시 참고

# f스트링 표현식, f로 표현 {} 변수 삽입해 표현도 가능 

# 3.불린형
# 참(True)/거짓(False)
True
true # 불린형 아님! -> 대소문자 유의 
print(type(is_male)) #bool

# 형 변환
# 내장함수 사용하여 변환
# int(변환하고 싶은 값)
# flaot()
# str()
# bool ()
# 바꿀 수 있을 때까지만, 변환 가능한 경우만

print(type(int('3'))) #가능
print(type(float('3/5'))) #불가능, 에러메세지 참고 

# 연산자
# '처리'
print('===연산자===')

#1. 산술연산자 (+,-,*,/,//,%,**)->숫자계산 모든 연산 
#2. 복합연산자 (+=,-=,*=,/=,//=,%=,**-)-> 산술연산+재할당(=)
#3. 비교연산자
# 값 두개를 "비교" -> True/False로 반환
# 대소비교 : <, >, <=, >=  (수치자료를 위주로 사용하는 것이 편리)
# 일치비교 : ==, != (자료형 크게 타지 않는다. 같나 아닌가만 가리면됨)
num1 = 10
num2 = 7
#문자의 비교경우, 10이 7보다 먼저와서 작다고 인식.
print(num1 < num2)

a = True
b = 'False'
print (a !=b)

# 조건문 / 반복문 하단에서 비교연산 많이 사용예정 

#4. 논리연산자 
# a and b : True, True -> True 그외, False
# a or b : 어느 하나라도 True 면 True 
# not a : 반대 
# 코딩테스트 단축평가시 속도 빠르게함. 연산 생략하니까. 

print(name='alex')
print(money>5)

if name == 'alex' and money > 100:
    print('부자 {name}, 안녕하세요!')
else:
    print('누구세요?')
    
# 조건문
# 콤마 : 와 들여쓰기 중요 

name = 'jun'
print(name)
print(money)

if name == 'alex' and money > 100: #False 
    print('부자 {name}, 안녕하세요!')
elif name == 'alex' : #True 
    print('alex 안녕하세요!')
else:
    print('누구세요?')
    print('장난입니다~') #1번 케이스(들여쓰기, 조건 맞을때 실행)

#print('장난입니다~') #2번 케이스 (들여쓰기에 따라 의도와 다르게 실행된다. 조건과 관계없이 실행)

# 중첩조건 
# if 여러개 