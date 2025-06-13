# 제어문 if, 반복문for 과 다양한 풀이 
gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]

# Q. 채굴한 광산 중 1등급 찾기(멤버십 연산자)
# 1. 멤버십 연산자 

print(1 in gems)

# 2. for문 + if 문 
for gem in gems:
    if gem == 1:
        print(True)
        break 
#true로만 물어봐서, T만 뜸

# Q. 등급별로 광물이 몇개 있는데? 

# 1. 딕셔너리
gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]
grades = {1:0, 2:0, 3:0} 
# key(등급):value(등급별갯수) 값 어떤 의미인지 모르겠음. 설정(등급,등급별갯수)필요
# 딕셔너리에서는 공백이거나 쌍으로만 존재해야함.

# 방법 1 
for gem in gems:
    grades[gem] += 1 
    
print(grades)
#[1: , 2: ,3: ]으로 표기

# 방법 2
# 비어있는 딕셔너리 이용할것
gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]
grades = {} 

for gem in gems :
    if gem in grades: 
    grades[gem] += 1 #Error 뜸. 더하고 재할당. 
else:
    grades[gem] = 1 # gem(리스트내 요소첫값)이 grade에 없으면 할당 
print(grades) 
# gems 리스트 내 요소 발견한 순서대로 등급별 갯수 기록됨! [3: ,2: ,1: ]

# 2. 리스트 (심화)
gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]
grades = [0,0,0] #[0]*3, 
#리스트는 비어있을때 추가시 []대괄호로 할당 힘듬. append 후 추가 재할당해야함.
#리스트 컨테어니 [] 상자가 있을때는 변경시 재할당 
#딕셔너리는 순서가 없기에 그냥 [] 추가 가능.

for gem in gems:
    grades[gem-1] += 1 

print(grades)

    
# 2방법중 딕셔너리가 훨씬 편함. 직관적. 그러나 문제해결 다양한 접근방법 제시. 