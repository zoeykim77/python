# 객체지향 프로그래밍 
# 객체에 딸린 변수는 '속성', 객체에 딸린 함수는 '메서드'
# 클래스에서 생성된 객체는 '인스턴스'
# 절차지향보다 간단하게, 각 조건에 따른 행동에 나오는 결과값 분리해 쉽게 파악!

# 장점 1 : 재사용, 유지보수성(모듈화) 
# 장점 2 : 확장성 (상속통해 기존클래스 두고 새 클래스 생성가능)

# 단점 1 : 설계가 어려움 
# 단점 2 : 디버깅 어려움 

class Student: # 학생설계 
    status = '피곤함' #글로벌리 이런 속성? 
    popultation = 0 
    
    def __init__(self, name, age, weight):
        self.name=name
        self.status=Student.status #피곤함이란 속성 바뀔수도?
        self.weight=weight 
        self.level=0 # 초기에서 입력받지 않은 값도 넣을 수 있다. 
        Student.population +=1 # 생성자가 하나씩 증가될 때마다, 인구수 1씩 증가 
        
    def study(self): # 공부하는 행동 (메서드)
        self.level += 1 # 객체의 속성,결과 바뀜  
    
    def intorduce(self): #소개
        print(f'저는 {self.name}, 학생이죠.')
    
    def eat(self): 
        self.weight +=1 
        
    #or 조건에 따라 행위 따른 결과값 다르게 조정 가능! 
    def eat(self, menu):
        if menu == '오므라이스':
            self.weight += 0.5
        elif menu == '부대찌개':
            self.weight += 1.5
        else: 
            self.weight +=1 
        
    def run(self):
        self.weight -=1 
    
student1 = Student('짱구',10)
print(Student.popultation) # 1 나옴 

print(student1.level) # 0

student1.study() #+1
student1.study()
student1.study() # 공부 계속하면 +3

print(student1.level) # 3이 됨 

student1.eat() # 먹는 행위 +1
print(student1.weight) # 11

student1.eat('오므라이스') # +0.5

student1.run() # 뛰는 행위 -1 
print(student1.weight) # 10 

