'''
[Question 2] = (20점)
한 반 학생들의 이름과 수학 점수가 담긴 2차원 리스트가 주어질 때, ex) [이름, 점수]
수학 점수가 가장 높은 사람의 이름을 출력하시오.
'''

scores = [['alex', 30], ['rachel', 25], ['fred', 50], ['june', 80],
          ['jane', 90], ['elle', 40], ['ken', 65], ['jun', 85],
          ['chelsea', 60], ['gorden', 75], ['kelly', 100], ['kate', 55],
          ['jacob', 15], ['harry', 70], ['haley', 55], ['kyle', 95]]



# 정답 = 내답 
# scores 리스트 안의 리스트, 2차원 리스트 
# 방법 1) 리스트 메소드 : sort메소드, labmda함수(정렬)

# 방법 2) 리스트 갱신 값 얻기 : 초기값 설정, 변수 2개 설정, 할당연산자 왼쪽 위치 중요! 

best_score=0
best_name=""
    
for name, score in scores:
    if best_score < score:
        best_score = score
        best_name = name
print(best_name)

# 내답 
scores.sort(key=lambda x:-x[1])
best=scores[0][0]
print(best)
