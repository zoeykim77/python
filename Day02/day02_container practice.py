#컨테이너 자료형 연습
## 리스트
#1. a 라는 리스트 선언. 이때 값은 1,2,4,5,7 순서대로 
#2. a 라는 리스트 가장 마지막 위치 10 추가 
#3. a의 가장 첫번쨰 위치값 삭제 
#4. 각 과정 거치며 a의 주소값 확인한다. 

#리스트의 특징 -> 순서o, 변경 o 
a = [1,2,4,5,7]
print(a)
print(type(a))
print(id(a))

#값추가 
a.append(10)
print(a)
print(id(a))

#값삭제
a.pop(0) # 추가/삭제는 [] 아니고 (), 인덱싱/슬라이싱 []
print(a)
print(id(a))

## 문자열
#1.알파벳 소문자 붙은 문자열 입력으로 받아,각 글자를 원소로 갖는 리스트로 변환하여 출력
#2.문자열 입력받아, 해당 문자열아 해당 문자열이 펠린드롬인지 아닌지 판별하라. 
#3.문자를 앞으로 읽은것과 거꾸로 읽은 것이 같은 단어를 펠린드롬. 

# 입력으로 받아, 문제 제대로 이해! 
word = input('단어를 입력해주세요')
print(type(word)) #str 
print(id(word))

#리스트 변환해 재할당
word = list(word)
print(word)
print(type(word))
print(id(word))

#문자열 슬라이싱 + 비교 연산자 
word = input('단어를 입력해주세요.')
print(word[::-1]) #슬라이싱, 거꾸로 뒤짚어 표현 
print(word == word [::-1]) #비교연산자 활용, 앞/뒤로 읽었을때 같은지 확인, ==연산은 T/F 함수

if word == word[::-1]:
    print('펠린드롬입니다')

else:
    print('펠린드롬이 아닙니다')

