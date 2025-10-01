# 문자열 메서드 실습
# (1)
# 오늘은 벚꽃축제 시즌!
# 카페 이벤트 메시지를 출력할 때, 모두 대문자로 출력해야 한다고 합니다.
# 아래 메시지를 모두 대문자로 변환하는 코드를 작성하세요

event_msg = "Welcome to Spring Blossom Festival!"

result=event_msg.upper() #새로 result생성(변경불가니), upper 메소드 치트키 
print(result)

event_msg = event_msg.lower() # 소문자화 
event_msg = event_msg.capitalize() #첫글자만 대문자 
event_msg = event_msg.title() #타이틀화, Wel~ To~ The 
#재할당필요??? 새로 result 생성 안해도, 기존 even_msg를 메소드 붙인걸로 대체해도 됨 

# (2)
# 리뷰를 확인하던 중, 어떤 손님이 오타를 내셨습니다.
# 아래 리뷰에서 'lattee'라는 잘못된 단어를 'latte'로 바꾸는 코드를 작성하세요

review = "The best lattee I have ever had."

review_r=review.replace("lattee","latte") # 재할당필요! (수정불가니까!)
print(review_r) 

# (3)
# 카페에서 이벤트 응모자를 공백(스페이스) 기준으로 나눈 리스트가 필요합니다.
# 응모자 명단을 리스트로 변환하세요.
applicants = "KimMinho LeeJisoo ParkSunghoon"

new_app=applicants.split(' ') #''만 하면 안됨, '  ' 반드시 스페이스로 공백 만들기! 
print(new_app)

# (4)
# 주문 내역에 고객 이메일이 기록되어 있습니다.
# 이메일 주소에서 아이디(골뱅이 앞부분)만 추출하는 코드를 작성하세요.
email = "cafe_guest21@blossom.com"

# 방법1 - split 활용 
print(email.split('@')[0]) #@ 구분한 리스트-> 첫번째 값만 
#기존 것 구분하니 그대로 print? 왜 새로 재할당안해줌?
 
# 방법2 - 슬라이싱 활용 
idx = email.find('@') 
print(email[:idx]) #간단하게!

# 오답 - why????
print(email.rstrip("@")) #앞이나 뒤에 @가 있으면 삭제. 

# 마찬가지로 기존에서 구분만 해주면 재할당 불요?