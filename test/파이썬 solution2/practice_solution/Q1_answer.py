# 다음의 리스트에서 소숫점을 제외한 평균값을 구하시오. ex) 3.1724일 경우 3을 출력
nums = [1, 7, 2, 3, 6, 1, 2, 5, 3, 4, 8, 7]

# 풀이 1
mean = sum(nums) / len(nums)  # 합산에서 길이를 나누면 평균!
answer = int(mean)
print(answer)  # 소숫점을 제외하기 위해 float 값을 int값으로 형변환 한다.

# 풀이 2
numerator = denominator = 0  # 분모와 분자를 각각 0으로 초기화 한다.
for num in nums:
    numerator += num  # 분자에는 숫자 자체를 더하고
    denominator += 1  # 분모는 1개씩 카운트를 해준다.

answer = int(numerator / denominator)  # 정답은 분모 / 분자
print(answer)

# 풀이 3
total = 0
for idx, num in enumerate(nums):  # 뚜껑 번호의 마지막은 idx => 11이 할당됐을 것이다.
    total += num  # 전체 합산을 하나씩 하고

answer = int(total / (idx+1))  # 나눠줄때는 뚜껑번호 + 1 을 해줘야 nums의 총 길이인 12가 된다.
print(answer)
