# 카운트 다운 있는 로또 추첨기 만들기 
import random
import time


# 오답 (내답)
import random
number=random.sample(range(1,45),6)
print(number)

import time
lotto = []

for i in range(5):
    time.sleep(1)
    lotto.sort(reversed)
    print('f{i}초 남았습니다')

    

# 정답 (random, time은 이미 지정됨)
# 출력값 먼저 for문 구성 : 거꾸로 숫자 나오는걸 어렵게 생각함. 
for i in range(5):
    print(f'{5-i}초 남았습니다.') #reverse 정렬 아닌 ! 
    time.sleep(1)

# 리스트화, 숫자 넣어주기 : 빈리스트 불요. 
# .sample이나 .randint .sort 등 자유롭게 써서 

lotto=list(random.sample(range(1,46),6)) 
print(lotto)

# random.randint(1,45)가능, 그러나 똑같은 숫자 나올 수도 있다. 
# lotto.sort() 쓰면 오름차순 정리 가능 


