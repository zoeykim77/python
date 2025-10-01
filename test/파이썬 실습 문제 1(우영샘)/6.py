# 문제: 다음 판매 데이터에서 기본 통계 정보를 계산하세요.
# 최댓값, 최솟값, 합계, 평균을 구하세요.

sales_data = [120, 85, 200, 150, 95, 175, 110, 165, 140, 185, 90, 155]


# 리스트의 최댓값, 최솟값, 합계, 길이를 구하는 방법을 탐색하세요.
# 여기에 코드를 작성하세요

print(max(sales_data))
print(min(sales_data))
print(sum(sales_data))

max = -999

for i in sales_data:
    if max <= i:
        max = i

print(f"최대값 :{i}"


min = 999

for i in sales_data:
    if min >= i:
        min=i

print(f"최소값: {i}")


total = sum(sales_data)

print(f"합계: {total}")

average = float(sum(sales_data)/len(sales_data)
print(f"평균: {average}")


# 출력 예시
# 최댓값: 200
# 최솟값: 85
# 합계: 1670
# 평균: 139.17