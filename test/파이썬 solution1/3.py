# 문제: 다음 점수 리스트에서 80점 이상인 점수만 필터링하고,
# 각 점수에 5점씩 더하기 한 값을 모아서 새로운 리스트를 만들어서 출력하세요.

scores = [75, 82, 91, 68, 95, 73, 88, 79, 92, 85]

# for문과 if문을 사용해서 필터링하세요.
# 해답 코드
filtered_scores = []
for score in scores:
    if score >= 80:
        filtered_scores.append(score + 5)

print(filtered_scores)

# 출력 예시
# [87, 96, 93, 97, 90] 