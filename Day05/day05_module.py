# 기초 내장 모듈
# 1) random 모듈 
# 무작위로 무언가를 뽑을때, 사용되는 모듈 

import random

# random.메소드 검색시 다양한 기능 나옴 

# random 랜덤 숫자 뽑기(리스트x 범위중에서) 
num=random.randint(1,5) #range 중에 무작위로 뽑기, random하게 int 뽑기  
print(num)

# choice 랜덤한 목록중에 하나 뽑기 (리스트 내 요소중 랜덤하게 하나씩 추첨)
nums = [1,5,10,21]
num=random.choice(nums)
print(num)

# (추가하기)
nums.extend([7,8,9])

# sample 원하는 갯수만큼 샘플 뽑기 (리스트 중 몇 개만 뽑기)
samples = random.sample(nums,2)
print(samples)

# shuffle 무작위 섞기 (리스트 내 요소 무작위섞은후 리스트로 반환)
random.shuffle(nums)
print(nums)

# 로또 추첨기, 발표자 뽑기, 티켓 추첨, 랜덤 조뽑기 등등 

# 2) time 모듈 
# 시간을 다루는 모듈 
import time

# time.sleep 함수 : 몇 초 기다린후 출력되게 함 

print('한숨 자겠습니다.')
time.sleep(10) # 숫자가 의미하는 바, ()초동안 동작정지
print('일어났다!')

#추가 예시 
for i in range(5):
    time.sleep(1) # 숫자가 의미하는 바, (1)초동안 동작정지
    print(f{i}초 기다린후, {i} 출력')

# 로또추첨 / 팀배정 -> 두구두구, 1초씩 기다린 후 출력 