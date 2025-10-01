# 랜덤 밥먹기
students = ['성우님', ' 민지님', ' 주용님', ' 현근님', 
            '나라님', ' 민석님', ' 연준님', ' 근찬님', 
            '재룡님', ' 한별님', ' 정원님', ' 혜지님', 
            '승찬님', ' 재훈님', ' 유정님', ' 우진님']

# students가 다음과 같이 주어졌을 때,
# 랜덤 밥먹기 조를 배정하는 프로그램을 짜 보세요!

# 내 답 : 인원중복될 가능성 / if문 불요 / 현재 16번의 랜덤. 

import random

team1=random.sample(students,4)
team2=[]
team3=[]

for i in students:
    if i not in team1:
        team2=random.sample(students,4)
    else:
        team3=random.sample(students,4)

print(team1,team2,team3)

# 정답 여러가지 가능! 
# 스스로 구조화가 필요 

# 방법 1) random->sample??
# 어렵다.. + for문 2번 

team=[] #리스트 생성
for i in students(len(students)//4): # 4명씩 1조
    people = random.sample(students,4)
    team.append(people)
    for person in people:
        students.remove(person)
        
print(team)
print(len(team))

# 방법 1)의 오답 
for i in students(len(students)//4): ## 4명씩 나누어 잘라준다.
    team = random.sample(students,4)
    print(team) #동일인 여러 조에 들어갈 수 있다.


# 방법 2) random ???
# 딕셔너리에서, 한팀에 인원수 많으면 알아서 조정 

team ={} #딕셔너리 생성 
for i in range(1,5):
    team[i] = []

available_team=list(range(1,5))

for student in students:
    team_num = random.choice(available_team)
    team[team_num].append(student)
    
    if len(team[team_num])>=4:
        available_team.remove(team_num)

# 방법 2) 오류  
    team[random.choice(range(1,5))] #1-4조까지, 그냥 갱신만됨 

# 방법 3) shuffle

random.shuffle(students)

team_size=4
team_lst=[]

for idx in range(0,len(students), team_size) # team size=4range 내 슬라이싱
    team_lst.append(students[idx:idx+team_size]) #슬라이싱, 지금위치에서 4간격

# 방법 4) 집합으로 


