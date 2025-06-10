# 연습문제풀이
# 1번문제

weight = float(input("몸무게를 입력해주세요 (단위:kg):")) 
# 실수로 변환 필요, #input에 프롬프트"""
#변수는 영문
height = float(input("키를 입력해주세요 (단위:m):")) # m 단위임을 파악

print(weight,height)
print(type(weight),type(height)) # str 인식 -> float 실수형 변환필요


#BMI계산식
bmi = weight / (height * height) # 수학계산식, 우선순위끼리 ()묶어줘야함.
print(bmi)

#조건문
if bmi >= 25:
    print('비만')
elif bmi >= 23: 
    print('과체중')
elif bmi >= 18.5:
    print('정상')
else:
    print('저체중')
    
    
#새연습문제 (0610)

