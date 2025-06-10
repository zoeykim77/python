# range 연속된 정수목록 
print(range(1,11)) #1-10까지 출력 

# range 특징 1 : 순서가 있는 정수목록
# 인덱싱, 슬라이싱하여 볼 수 있다. 
number = range(1,11) #세로로 길게뜸, 리스트 형태로 바꿔준다 #끝숫자 생략 ??
print(list(number)) 
print(number[1]) #인덱싱 가능
print(number[1:3]) #슬라이싱 가능 (시작, 끝, 간격 생성)

# range 특징 2 : 불변 자료형 (변경불가)

# 주요사용법 
for i in range(1,11):
    print(i)
# ?? for문은 무엇인가 
 