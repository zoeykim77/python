# 실습 : 입금과 출금, 조회 

# 정답
class BankAccount : #객체생성 
    # 인스턴스 생성 
    def __init__(self, account_holder, balance=0): # 밸런스는 디폴트는 0, 수정가능케 형성
        self.account_holder=account_holder
        self.balance=balance # 속성을 할당 
    # 메서드 생성 
    def desposit(self, amount): #값 2개로 넣어줘야함! self, amount
        self.balance+=amount 
    
    def withdraw(self, amount): 
        self.withdarw-+amount 
    
# 객체 생성 및 메서드 호출
account = BankAccount("홍길동") #balance 값 =0 은 초기값설정, 여기서 안넣어도 됨

# 잔액 조회

# 입금
account.deposit(1500)
print(account.balance)
print(f'현재 잔액: {account.balance}원')

# 출금 ** 유효성 검사 필요하다! ** 
account.withdraw(300)
print(account.balance)
print(f'출금 {amount} 되었습니다. 현재 잔액: {account.balance}원')

# 잔액 조회
account.withdraw(1200)
print(f'현재 잔액: {account.balance}원')

# 계좌소유자 조회 
print(f"계좌 소유자: {account.account_holder}")


# 내답 
class BankAccount:
    balance = 0 # def __ init__생성자 메서드 아닌 초기값? 
    
    def __init__(self, account_holder, balance): 
        self.account_holder=account_holder
        self.balance=balance
    
    def deposit(self, amount):
            self.balance+=amount

    def withdraw(self, amount):
            self.balance-=amount
            
account = BankAccount("홍길동",0) # 값 2개 넣어야 생성됨 

account.deposit(1500)
print(account.balance)
print(f'현재 잔액: {account.balance}원')

account.withdraw(300)
print(account.balance)
print(f'출금 {amount} 되었습니다. 현재 잔액: {account.balance}원')

account.withdraw(1200)
print(f'현재 잔액: {account.balance}원')

print(f"계좌 소유자: {account.account_holder}")

# 유효성 검사

