# 통계_심화 : 실전, 기술통계! 
# Q1.중앙값 

prices = [300000, 350000, 400000, 450000, 500000, 550000, 600000, 5000000]

# 정답
# 방법 1
prices.sort() # 정렬 
print(len(prices)) #8, 짝수 갯수 확인 
print(prices[3]+prices[4]/2)
# 방법 2 : 인덱스 직접 구하지 않고 계산해 넣기 
print(prices[len(prices)//2-1]+(prices[len(prices)//2])) 

# 중앙값 vs 평균, 중앙값 구하는 이유는?
# 중앙값을 사용해야 하는 이유 : 이상치 영향 덜 받기 떄문 

print(sum(prices)/len(prices))

# 내답 
prices.sort()
print(prices)
print(prices[3]+prices[4]/2)


#Q2. 최빈값 (mode)

subjects = ["Python", "Java", "Python", "C++", "Python", "Java", "C++", "Python", "Data Science", "Data Science", "Python"]

# 정답 

# 방법 1 : 딕셔너리 이용 

subjects_cnt = {} 

for i in subjects_cnt:
    if i not in subjects_cnt.keys(): #딕셔너리 키로 나타내야함 
        subjects_cnt[i] = 1 #초기화 
    else:
        subjects_cnt[i] += 1 
print(subjects_cnt)

# 방법 1-1. 
best_sub = ""
best_cnt = 0

for sub, cnt in subjects_cnt.items():
    if cnt>best_cnt:
        best_cnt = cnt
        best_sub = sub 
print(f'최빈 과목은 {best_sub}, 나타난 횟수는 {best_cnt}이다')

#방법 1-2 : sort로 정렬 


# 방법 2 : 내장모듈 collections 의 Counter 함수 (자동 갯수세기)
from collections import Counter  
result = Counter(subjects) 
print(result.most_common(1)) #.most_common()으로 가장 보편적 값 도출  

# 내 답 
sub = {} 

for i in subjects:
    if i not in sub:
        sub[i] = 1
    else:
        sub[i] += 1
        
print(sub)
print(sorted(sub, reverse=True)[0]) #리스트로 치환, 갯수 안나옴 



#Q3. 범위와 사분위수 범위

scores = [55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 37, 40, 20, 10, 90]

# 정답 
# 범위는 동일, 사분위수 구하기!
# 사분위수 공식 : 3사분위 - 1사분위 (중앙값 기준 범위)
# 방법 1 : 
scores.sort() #정렬 
len(scores) #길이 확인, 15
print(scores[len(scores)//2]) #중앙값, 8번째, 인덱스는 [7]

Q2 = scores[len(scores)//2] # 중앙값 기준 앞뒤 나누기
Q1 = scores[3]
Q3 = scores[-4] 

IQR = Q3-Q1 
print(IQR) # 50

# 방법 2 : 가상환경 구축후 np 인스톨? 
import numpy as np
Q1 = np.percentile(scores,25)
Q3 = np.percentile(scores,75)

print(Q3-Q1)

# 내답 
#범위 
scores_range = max(scores)-min(scores)
print(scores_range) #90

#사분위수 : 계산 어려움 
scores.sort()
print(scores) 
print(len(scores)) #15 
print(scores[7]) #70

print(scores[3])
print(scores[11])
print(scores[11]-scores[3]) #50


#범위 vs 사분위수와의 차이? 90 vs 50. 분포도 차이크다. 
# 범위는 전체 데이터의 데이터 흩뿌려진 범위, 사분위수는 중앙값에서의 분포 

#Q4. 분산과 표준편차 
# 분산과 표준편차의 차이? 
# 공식 체크 

A = [70, 75, 80, 85, 90]
B = [70, 80, 80, 80, 90]


# 정답 
# 평균구하기 (중심경향치) 같다. but A,B는 같은 데이터는 아니다. 
AVE_A = sum(A)/len(A) #80
AVE_B = sum(B)/len(B) #80 

# 분산구하기 
# 분산값은 A 50, B 40 으로 다르다.

A_var = 0 # 분산값 선언 필요(초기값 설정 )

for a in A : 
    A_var += (a-AVE_A) ** 2 

A_var /= len(A)
print(A_var) # 50


B_var = 0 

for b in B : 
    B_var += (b-AVE_B) ** 2 

B_var /= len(B)
print(B_var) #40 

# 표준편차 구하기 : 분산의 제곱근 

A_std = A_var **0.5 #제곱근 구하기 공식 
B_std = B_var **0.5 

print(round(A_std,3)) #7.071
print(round(B_std,2)) #6.325

# 평균 같지만, 표준편차가 적은 B가 더 일관된 성적을 보이고 있다는 것을 파악 가능.

# 내 답 
AVE_A = sum(A)/len(A)
AVE_B = sum(B)/len(B)
print(AVE_A)
print(AVE_B)

# 방법 1 
variable_A = sum((i-AVE_A)**2 for i in A) / len(A)
variable_B = sum((i-AVE_B)**2 for i in B) / len(B)

print(f"A의 분산: {variable_A}")
print(f"B의 분산: {variable_B}")

#방법 1의 오답 :
# for i in A:
#    variable_A=sum((i-AVE_A)**2)/len(A)
# print(variable_A)
# 왜 float은 순환이 안된다고 하지?, for 문을 왜 뒤에 넣지? 

# 방법 2 

variable_A = []
standard_A = []
variable_B = []
standard_B = []

for i in A : 
    variable_A.append((i-AVE_A)**2)

result_A = sum(variable_A)/len(variable_A)
print(result_A) #50

for i in A : 
    standard_A.append((i-AVE_A)**0.5)
result2_A = sum(standard_A)/len(standard_A) #0

print(result2_A,2)

for i in B: 
    variable_B.append((i-AVE_B)**2)

result_B = sum(variable_B)/len(variable_B)
print(result_B) #40 

for i in B : 
    standard_B.append((i-AVE_B)**0.5)
result2_B = sum(standard_B)/len(standard_B)
print(result2_B) #0


# Q5. 왜도와 첨도 적용 
# 평균이 8, 표준편차 2 
# 대부분 고객 5-11페이지 사이 클릭, 소수 고객 20페이지 이상 클릭
# 데이터의 왜도 추정, 추정치는 분석에 어떤 통찰?

# 양의 왜도, 대부분 일반 패턴, 일부고객 예외 패턴. 
# 양의 왜도는 헤비유저 집단, 별도 분석해 리마케팅 / 추천 /VIP 혜택 설계 가능 
