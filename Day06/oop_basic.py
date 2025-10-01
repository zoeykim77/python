# 객체지향프로그래밍 (oop)
# 파이썬에서 모든 것은 "객체"다! (절차가 아닌, 객체가 가진 정보와 속성으로!)

# 객체는 정보(속성,attribute)를 가지고 있고,
# 객체는 행동(메서드)를 할 수 있다.

# 그 객체를 만들기 위해 class라는 설계도를 만든다.

class Person: # 신처럼 사람이라는 객체 빚는다 
    species = '호모사피엔스' # 모든 객체가 속하는 상태 
    
    def__init__(self, name, init_age): # 초기정보, 인스턴스 만들때 꼭 넣어줘야 함! 
        self.name=name
        self.age=init_age 

    def introduce(self): # 소개 메서드
        print(f'안녕하세요, 저는 {self.name}입니다.') 
    
    def birthday() # birthday 메서드로 속성 변화 
        self.age +=1
        
student = Person() #오류뜸, init내 정보 넣어야 함 
student = Person('alex',3)
print(student.age) # 정보(속성) 

student.introduce() # 행동 

student.birthay()
print(student.age) # 생일 지난뒤 나이 +1 로 속성변화 

student.species # class 값인 '호모사피엔스'출력, 모든 인스턴스가 공유하는 속성(정보값)

# 객체에 딸린 변수는 '속성', 객체에 딸린 함수는 '메서드'
# 클래스에서 생성된 객체는 '인스턴스'
# 절차지향보다 간단하게, 각 조건에 따른 행동에 나오는 결과값 분리해 쉽게 파악!

# 장점 1 : 재사용, 유지보수성(모듈화) 
# 장점 2 : 확장성 (상속통해 기존클래스 두고 새 클래스 생성가능)

# 단점 1 : 설계가 어려움 
# 단점 2 : 디버깅 어려움 