# 문자열
# 0개 이상의 문자를 순서가 있게 저장하는 컨테이너 자료형이다. 

name = 'python'
print(name)
print(type(name))

# 문자열 특징 1 : 순서가 존재한다.
# 인덱스(위치)로 값 확인 가능하다.

#값조회 (인덱싱으로)
print(name[0])

#슬라이싱
print(name[0:2])

# 연산이 가능하다.
# 연산결과, 새로운 문자열이 생긴다.

# + 연산 : 문자열 + 문자열 
word1 = 'hello'
word2 = 'python'
print(word1+word2) #공백없이 문자가 이어짐 

# * 연산 : 문자열 * 반복횟수(숫자)
print(word2 * word1) #불가 int 타입 아니라서.
print(word2*3) #python 3번 반복해 나옴 

# 문자열 특징 2 : 불변 자료형 (수정불가, 추가/삭제도 안됨)
word1[0] = 'c' #불가
word3 = 'c' + word2[1:] # 새로운 문자열 추가해, 연산작성은 가능 
print(word3)
