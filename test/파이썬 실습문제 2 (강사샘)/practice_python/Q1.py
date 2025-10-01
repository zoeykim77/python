# 다음의 리스트에서 소숫점을 제외한 평균값을 구하시오. ex) 3.1724일 경우 3을 출력
nums = [1, 7, 2, 3, 6, 1, 2, 5, 3, 4, 8, 7]

n=0

for num in nums:
    n+=1

result=int(n/len(nums))
print(result)


# print(answer) # 4