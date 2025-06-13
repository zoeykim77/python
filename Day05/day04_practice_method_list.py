# 1
# 카페에서 판매 중인 음료 메뉴가 아래와 같이 리스트로 저장되어 있습니다.
# 어느 날, "딸기라떼"가 신메뉴로 출시되어, 'americano' 뒤에 추가해야 합니다.
menu = ["americano", "latte", "cappuccino"]
menu.insert(1,"strawberry latte")
print(menu) 
## 오답 : 절대, print(menu.insert(1,"strawberry latte"))하지 않기.
##       menu.메소드는 리스트를 메소드함수로 수정하는 행위임(결과x,함수박스내부) 
##       print(menu) 결과 확인 가능, 결과는 리스트를 요청해야함. 

# (2)
# 어느 손님이 “오늘 라떼는 빼주세요”라고 요청했습니다.
# 메뉴에서 'latte'를 삭제한 뒤, 
# 삭제한 메뉴가 실제로 삭제되었는지 True/False로 확인하는 코드를 작성하세요.

menu.remove("latte")

if "latte" not in menu:
    print('T')
else:
  print('F')

# pop으로 삭제원해? index(요소값)으로 추가설정해 가능! 
menu.pop(menu.index('latte')) 

# 멤버십 연산으로 더 간단히 확인 가능, T/F로 반환하니까!  
'latte'not in menu
print('latte'not in menu)

# (3)
# 오늘 아침 재고 조사를 했더니, 기존 메뉴에 빵 리스트가 따로 있다는 사실을 알게 되었습니다.
# 음료 리스트와 빵 리스트를 합쳐, 하나의 ‘통합 메뉴판’ 리스트로 만드세요.

bread = ["bagel", "croissant", "scone"]

#1. 리스트 복합연산 +로
new_menu = menu + bread # 새 리스트 생성, id 달라짐! (but 기존리스트에 +[] id동일)
print(new_menu)

#2.extend 메소드로 
menu.extend(bread) # extend() 안에는 리스트가 들어온다, 메소드는 id 같음!


# (4)
# 카페 점주님이 메뉴의 가나다순 정렬을 원하십니다.
# 통합 메뉴판을 오름차순으로 정렬하는 코드를 작성하세요.

# 방법 1 
new_menu.sort()

# 방법 2
new_menu = sorted(new_menu) 

# 내답 
sorted_list=new_menu.sort() # 오답 
new_menu.sort() #sorted 함수와는 다름, .sort 메소드로 사용! 
print(new_menu) 