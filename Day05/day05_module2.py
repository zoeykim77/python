# 모듈 불러오기 
# import 로 모듈 불러오기  
import module1

# from만 써서 모듈의 일부 불러오기 
from module1 import add, subtract # 모듈 1에서 add라는 함수만 가져올 수 있다. 
from module1 import * # a모두 가져올 수 있다. 
from module1 import subtract as sub #별칭 (넘 길면 줄여서)

# 함수 호출, 새로 사용가능 
print(module1.add(1,4)) # 정석 
print(add(1,4)) # 간단히 작업해 호출 
print(sub(1,5)) # 별칭으로 호출 


