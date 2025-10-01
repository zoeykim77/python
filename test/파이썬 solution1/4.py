# 문제: 다음 점수 리스트를 기반으로 각 점수에 대한 등급을 분류하세요.
# 90점 이상: "A", 80점 이상: "B", 70점 이상: "C", 그 외: "F"
# 결과를 딕셔너리로 출력하세요. {점수: 등급}

scores = [95, 87, 76, 92, 68, 83, 91, 74, 89, 65]

# 조건문을 사용해서 점수에 대한 등급을 분류하고, 딕셔너리에 저장하세요.
# 해답 코드
grade_dict = {}
for score in scores:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
    
    grade_dict[score] = grade

print(grade_dict)

# 출력 예시
# {95: 'A', 87: 'B', 76: 'C', 92: 'A', 68: 'F', 83: 'B', 91: 'A', 74: 'C', 89: 'B', 65: 'F'} 