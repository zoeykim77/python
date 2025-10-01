# 문제: 다음 판매 데이터에서 기본 통계 정보를 계산하세요.
# 최댓값, 최솟값, 합계, 평균을 구하세요.

sales_data = [120, 85, 200, 150, 95, 175, 110, 165, 140, 185, 90, 155]

# 리스트의 최댓값, 최솟값, 합계, 길이를 구하는 방법을 탐색하세요.
# 해답 코드
max_value = max(sales_data)
min_value = min(sales_data)
total_sum = sum(sales_data)
average = total_sum / len(sales_data)

print(f"최댓값: {max_value}")
print(f"최솟값: {min_value}")
print(f"합계: {total_sum}")
print(f"평균: {average}")

# 출력 예시
# 최댓값: 200
# 최솟값: 85
# 합계: 1670
# 평균: 139.16666666666666