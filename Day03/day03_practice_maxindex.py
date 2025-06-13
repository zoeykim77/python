# 최고, 최저 매출 일자 파악하기 
sales = [2000, 3000, 4000, 1000, 1500, 3800, 200, 2900, 1300]

# 구조화 1 (변수 4개로 선언) -> 기준해설 / 왜 for문에 초기값? 
max_sales = -999 #가장 작은수로 최대값설정
max_date = 0 
min_sales = 9999
min_date = 0

#for 문
for sale in sales:
    if sale > max_sales :
        max_sales = sale 
        max_date = #??? 리스트니까, 위치 인덱스를 받자 
        
#date 를 인덱싱으로 찾아 다시해보기         
for idx in range(len(sales)):
    if sales[idx] > max_sales:
        max_sales = sales[idx]
        max_date = idx + 1 #range, index 0부터 시작하기에! 
    if sales[idx] < min_sales 
        min_sales = sales[idx]
        min_date = idx + 1 # max 작업후, 조건 if 붙여 바로 min 작업가능! 
        
print(max_sales)
print(max_date)
print(min_sales)
print(min_date)

print(f'최고매출: {max_date}일차, {max_sales}만원')
   
# 구조화 2 (변수줄여서, 딕셔너리로)
sales_summary = {'max_sales': -999,
                 'max_date':0,
                 'min_sales':9999
                 'min_date':0}

sales_summary = {'max_sales': sales[0],
                 'max_date':1,
                 'min_sales':sales[0],
                 'min_date':1} 
print(sales_summary)

for idx in range(1,len(sales)):
    if sales_summary ['max_sales'] < sales[idx]:
        sales_summary ['max_sales'] = sales[idx]
        sales_summary ['max_date'] = idx + 1
    if sales_summary['min_sales'] > sales[idx]:
        sales_summary['min_sales'] = sales[idx]
        sales_summary['min_date'] = idx+1

print(f'최고매출: {max_date}일차, {max_sales}만원')

# 구조화 3번째(위 문제 훨씬 간단히 표기) 
for idx, sale in enumerate(sales):
    print(idx, sale)
#순서(인덱스)와 값 하나씩 나열됨 

for idx, sales in enumerate(sales):
    if sales_summary['max_sales'] < sale: #인덱싱하지 않아도 됨 
        sales_summary['max_sales'] = sale
        sales_summary['max_date'] = idx+1 
    if sales_summary['min_sales'] > sale:
        sales_summary['min_sales'] = sale
        sales_summary['min_date'] = idx+1


