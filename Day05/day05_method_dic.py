# 딕셔너리 
# 특징 1 : 순서 x =
# 특징 2 : 가변자료형 (mutable)
# {} 로 표현 / key:value 쌍인 항목, 각 쉼표로 구분 
# key는 유일 (숫자형, 불리언, 문자열, 튜플 등 변경불가형)
# value는 다양한 자료형 가능스
# key를 기준으로 값에 접근!

students = {'kyle':10, 'jun':20, 'alex':30}

# 값 조회 기본 : key 기준으로 value 값 접근. (인덱싱처럼!)
# 딕셔너리 내 key가 존재할때만 출력!, 없는 key 조회시 키에러!(에러시 프로그램 멈춤) 
print(students['kyle']) 

# 1) get 값 조회 사용 메서드 : 각 값으로 조회 
students.get('justin') # none
# 딕셔너리 내 없는 key 조회시 none으로 뜸, 에러 x 넘어감  
students.get('justin','Unknown key') #Unknown key
# 딕셔너리 내 없는 key를 , 이하 문구로 반환 / 에러x 넘어감 

# 가변 자료형 - 딕셔너리 
# 변경 추가 삭제 가능 

# 2) pop 삭제 : 리스트와 동일함 
# but  순서 있는 리스트완 다르게 pop(인덱스)->pop(key) 
students.pop('key') 

# 없는 키로 삭제요청시 에러 발생
# but 에러시 대치반환 지정 가능 (에러시 프로그램 멈춤수정)
students.pop('ela')
students.pop('ela',0)

# 3) keys,values, items : 키와 밸류로 조회 
students.keys() 
students.values()
students.items()

# class dict_keys, dict_values로 반환됨 -> 보기편하게 list화 가능
list(students.keys()) 

