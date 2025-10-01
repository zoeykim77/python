'''
[Question 3] = (30점)
<외톨이 고르기>
구슬치기 게임을 하려면 두 사람이 필요하다.
하나의 외톨이(깍두기)를 제외한 모든 사람은 자기만의 짝이 하나 더 유일하게 존재한다.
번호는 자연수라고 가정하며, 외톨이는 1명만 유일하게 존재한다고 가정한다.
아래의 nums1 예제에서 1, 2, 4, 5번은 각각 자신의 파트너가 존재하나, 3번만은 파트너가 없는 외톨이다.
외톨이를 구하여 반환하는 함수를 완성하고, 외톨이를 출력해보시오.
'''

nums1 = [2, 1, 3, 1, 4, 5, 2, 5, 4]
nums2 = [7, 3, 26, 13, 1, 3, 77, 7, 13, 1, 26]



# 정답 : 직관적이기 보다 문제를 고찰! 

# 1) 로직세우기 
# 다양한 for문 방법 존재 

solo = 0 # 초기화
team = {} # 빈 딕셔너리 

for num in nums1:
    if num in team:
    team[num]+=1 #변수값 num과 딕셔너리[key=변수] 헷갈리지 않기! 
else:
    team[num]=1

# or

team(num)=team.get(num,0)+1 # 딕셔너리 메서드도 사용가능 

# or 

for plyaer_num in team:
    print(plyaer_num)


for num, cnt in team.items():
    if cnt == 1: # 외톨이면
        solo=num 
        break # 답이 나오면 멈춰 
print(solo) 

# 2) 함수로 로직 구현하기 
# 들여쓰기(탭) 위치 조심!! 
# nums 자리는 변수로 바꿔줘야함, nums1,2 다 인자로 들어올 수 있게 

def find_solo(nums):
    solo = 0 # 초기화
    team = {} # 빈 딕셔너리 

    for num in nums: # num 변수, nums도 변수 
        if num in team:
            team[num]+=1 # 변수값=키가 지칭하는 value에 += 1
        else:
            team[num]=1

    for plyaer_num in team:
        print(plyaer_num)

    for num, cnt in team.items():
        if cnt ==1: # 외톨이면
            solo=num 
            break
    return solo
print(solo) 

# 내답 : 포기 

number={}


def find_solo(nums):
    for nums in nums1:
        if nums not in number:
            number[nums]=1
        else:
            number[nums]+=1
        if number[nums]==0:
            print (number.keys[i])

print(number)         
print(find_solo(nums1))  # 3 출력
print(find_solo(nums2))  # 77 출력
