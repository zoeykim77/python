if False:
    print('조건이 참입니다.')
    print('같은 들여쓰기 수준이라면')
    print('동일한 코드블럭입니다.')
print('무조건 실행하죠')

#age = int(input('나이를 입력해 주세요.'))
# if age >= 20:
    print('어른')
elif age >= 10:
    print('청소년기')
elif age >= 5:
    print('어린이')
else:
    print('영유아기')
    
money = float(input('소비금액 (단위:만원)')) 
count = int(input('구매횟수'))

condition1=money>=1000
condition2=count>=10 

if condition1 and condition2:
    print('Vip회원입니다')

elif condition1 or condition2:
    print('우수회원입니다')

else:
    print('일반회원입니다')
    