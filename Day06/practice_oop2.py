# 실습 : 계좌만들기 심화_ 유효성 검사 

class BankAccount:
    
    def __init__(self, account_holder, balance=0):
        self.account_holder=account_holder
        self.balance=balance
    
    def deposit(self, amount):
        if type(amount)==int and amount >0:
            self.balance+=amount
        else:
            print(f'잘못된 값입니다')
            
    def withdraw(self, amount):  # withdraw 메서드에서 막힘, 2문구 다 출력됨!
        if type(amount)==int and amount >0: # if 중첩문 잘 구조화 하기! 
            if amount <= self.balance: #중첩문 2개 위치만 바꿔도 다른 답나옴..
                self.balance-=amount
            else:
              print (f'잔액이 부족합니다')   
        else: 
          print(f'잘못된 값입니다')

account = BankAccount("홍길동")

# 계좌 초기잔액 
print(f'초기잔액: {account.balance}원') 

# 계좌 입 출금 
account.deposit("천오백원")

account.deposit(1500)
print(f'현재 잔액: {account.balance}원')

account.withdraw(-300)

account.withdraw(1200)
print(f'현재 잔액: {account.balance}원')

account.withdraw(1600)

print(f"계좌 소유자: {account.account_holder}")