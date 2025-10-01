# 문제: 다음 학생 데이터를 학년별로 그룹화하고, 각 학년의 평균 점수를 계산하세요.

students = [
    {"name": "김철수", "grade": 1, "score": 85},
    {"name": "이영희", "grade": 2, "score": 92},
    {"name": "박민수", "grade": 1, "score": 78},
    {"name": "최지영", "grade": 2, "score": 95},
    {"name": "정다은", "grade": 1, "score": 88}
]

# 리스트 내부 각 딕셔너리의 grade 키의 값을 활용해서 학년별로 점수를 모으고, 학년별 평균을 구하세요.
# 해답 코드

# 빈 딕셔너리를 만들어서 학년별 점수를 저장
grade_scores = {}

# for 반복문을 사용해서 각 학생의 데이터를 순회
for student in students:
    grade = student["grade"]
    score = student["score"]
    
    # 딕셔너리에 학생의 grade 값이 key로 존재하는지 판단
    if grade in grade_scores:
        # 존재하면 점수를 추가
        grade_scores[grade].append(score)
    else:
        # 존재하지 않으면 빈 리스트를 초기화하고 점수를 추가
        grade_scores[grade] = [score]

# 4. 최종적으로 각 학년의 점수 리스트에서 평균을 계산
grade_averages = {}
for grade, scores in grade_scores.items():
    average = sum(scores) / len(scores)
    grade_averages[grade] = round(average, 2)

print(grade_averages)

# 출력 예시
# {1: 83.67, 2: 93.5} 