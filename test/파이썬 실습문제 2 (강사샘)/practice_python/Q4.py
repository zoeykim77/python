# <별 찍기>
# 자연수 N을 입력받아, N줄까지 별을 출력하는 함수를 만드시오.
# 첫 번째 줄은 별이 1개이며, N번째 줄은 N개의 별이 찍혀야 합니다.

# ex) 만약 N이 3 이라면?
# *
# **
# ***

N = int(input(''))

def print_star(N):
    for i in range (1, N+1):
        print('*'*i)

print(print_star(N))
