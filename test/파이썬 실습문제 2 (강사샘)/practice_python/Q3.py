# 주어진 배열 안의 값을 전부 2배로 만드시오.
# ex) [7, 2, 3]의 경우 [14, 4, 6]이 되어야 합니다.
nums = [7, 2, 9, 8, 4, 3, 5]

list=[]

for n in nums: #if문과 for문 헷갈리지 않기! 
    list.append(n*2)
    
print(list)
    