# 4일차 복습 (함수)
# 함수(function)
students = ['주용','재훈']

# 1. 사용자 정의함수 
# 1단계 : 정의하기 (define)

def check(students): # 매개변수, input으로 다양한 값으로 들어올 자리(위리스트x 가능) 
    if '주용' in students:
        answer = '주용님은 출석했다'       
    else: 
        answer = '주용님은 출석안함'
    return answer # 반환값 문자열(return값, = 없는데 왜 =??)

# 2단계 : 실행,사용하기, 호출하기 (call)

answer = check(students)
print(answer)

# 매개변수, 반환값 여러개 가능 : 콤마, 로 / 왜 student list 인식?

def check(student_list, name): # 매개변수, input으로 다양한 값으로 들어올 자리(위리스트x 가능) 
    if name in student_list:
        answer = f'{name}님은 출석'     
    else: 
        answer = f'{name}님은 출석안함'  
    return answer # 반환값 문자열(return값, = 없음)

answer = check(students, '재훈')
print(answer)


# 2. 내장 함수 
# 함수계산 가능한 것만 됨 
# 모든 함수가 모든 자료형에 사용가능하진 않다
print(students) 
print(f'1분단 학생 수는 {len(students)}명 입니다.')

# print(sum(students)) #에러 발생, 모든 함수가 모든 자료형에 사용가능하진 않다

# len 함수 : 길이 size / 리스트 안의 리스트의 경우, 리스트를 1개 요소로 계산!

# sorted 함수 : 정렬된 "새로운 리스트"를" 반환 <-> .sort() 메서드랑 다름 id가!
# sorted(순회가능한 자료형) 리스트, 딕셔너리, 문자열 가능 
# 오름차순 기본, 내림차순 (자료형, reverse=True)

students_a = sorted(students) #리스트 
print(students_a)

print(sorted('python')) #문자열


# max, min, abs 
# map함수 (**)
string = "123456"
number_list = list(map(int, string))

# 매개변수와 반환값 유무 (***)
# 2) 매개변수 유, 반환값 무 : students.append('재룡') 메소드는 반환값x 
# 3) 매개변수 무, 반환값 유 : 
# 4) 매개변수 무, 반환값 무 : 정해진 처리만 하는 경우 

# 익명함수 lambda
# 사용자 정의함수 처럼 내가 만듬 -> 이름 붙일 필요 없다고 생각
# 1회성 사용 함수 

answer = (lambda x:-x)(-1) #x를 넣었을때 -x로 반환 ! 변수와 함께 쓸때 ()() 
print(answer)

# sorted와 같이쓰임 
example = [(0,2),(2,3),(1,4)] #리스트, 리스트 [0] 각 값 접근시 튜플 확인, 변경불가

len(example) #3
type(example) #리스트 

len(example[0]) #2 (a,b) 2개로 인식 
type(example[0]) # 튜플, 리스트 내부의 튜플, 변경불가  

example_a = sorted(example) #순회가능한 example을 정렬해 반환해줌. 첫째 기준 정렬 
print(example_a) 

example_b = sorted(example, key=lambda x:-x[1])
print(example_b)

# 정렬할 기준을 사용자지정, 익명함수로 설정가능
# key 기준값을 기준으로, lambda 함수로 사용 요소 x에 :-x[1] 
# lambda 적용시, 튜플 두번째 요소값에 -붙인값 기준으로 다시 오름차순!


# 컨테이너 자료형 - 리스트
# 1. 순서가 있다.(인덱스 0~n-1까지 접근가능)
# 2. 가변자료형, 변경가능하다. 
# 메서드 사용(리스트에 딸린 함수) : 같은 성격을 띔, 메서드로 수정해도 id는 같음 

numbers = [10,20,30,40,50]

# 추가 append : 메서드도 순서가 있어야 함(맨 끝에 요소가 추가됨)
numbers.append(60) 
# 요소 마지막에 추가, id 동일! (내장함수로 수정했으니)
# 나 자신 바꾸어 버림. 반환x 

# 삭제 pop : 인덱스(위치)를 기준으로 
numbers.pop(1)

# 삽입 insert : 위치를 기준으로 추가 
numbers.insert(1,200) #1위치(두번째자리)에 200넣기 

# 추가 extend : 여러개 값 추가 
numbers.append(1,2,3,4) #오류, append는 1개만 추가 가능! 여러개 x
numbers.append([1,2,3,4]) #리스트로 추가시, 리스트 뭉텅이로 마지막 요소로 추가

numbers.extend([1,2,3,4]) #리스트로 추가시, 여러 요소가 자연스럽게 추가됨

#리스트의 복합연산도 동일한 결과를 반환한다. 
numbers +=[1,2,3,4]  

# 삭제 remove : 값 기준 삭제 
numbers.remove(10) # 리스트 내 10 원소를 삭제함 (위치x)
numbers.remove(1000) # 리스트 내 없는 원소 삭제요청시 -> error! 

# 수세기 count : 값 기준으로 수 세어줘
# 나를 바꿀 필요가 없다. (숫자만 세니까)
cnt = numbers.count(1) # 1이란 원소가 몇개인지 세어줘 
print(cnt) #반환값, 즉 1이몇개인지 결과로 반환 
# 광물찾기 시험, for문 대신 간단하게 count로 가능 

# 위치 index : 해당값 위치 반환
numbers.index(1) 
# 1이라는 값의 위치를 나타내줌 
# 위치가 없으면 에러   

# 정렬 sort() 
# 정렬 안되는 경우, str 과 int는 비교불가하기에 정렬 불가해짐.
# 비교가능한 요소만 정렬! 

numbers.sort() # 정렬요청 
print(numbers) # 자동적용