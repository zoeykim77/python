# 떡잎마을 반장선거
# 후보가 없는 반장선거

votes = ['짱구','짱구','수지','짱구','훈이','맹구',
        '수지','수지','수지','짱구','유리','철수','수지']
result = {} #딕셔너리 

# 누가 반장이 되었을까요?
# 투표 내역을 하나하나 돌아가며, 값을 센다.
    #1) 해당 후보자가 표를 "득표" 했을때 
    #2) 표 내역에서 후보자 이름이 나왔을때, 
        #1) If 만일 후보자 등록이 완료된 경우에는 +1, 
        #2) else 만일 후보자 등록이 안되었다면 등록 후 1할당  

result['짱구'] = 1 # 생성가능 
result['짱구'] += 1 # 복합연산 불가, 짱구 조회단에서 에러. 없기에.
result['짱구'] = result['짱구'] + 1  
# 불가한 연산, result에서 짱구 못찾으니까. 

for king in votes:
    if king in result:
        result[king] += 1
    else:
        result[king] = 1 

print(result)

# 반대로     
for king in votes:
    if king not in result:
        result[vote] = 1 # 입후보시키기, key값 생성 
    else:
        result[vote] += 1 # 이미 후보면, 복합연산으로 누적 
    
print(result)

# 반장은 누구? 수지 원할시 (심화)

# 멤버십 함수는 key로 검색조건.
# 즉, value값 로만 검색하기 힘들다. 즉, 반장=수지로 바로나오는 값 도출 힘듬.
# 딕셔너리+멤버십에서는, value값 도출원할시 멤버십 대신 메소드를 사용했었음.  

result_lst = list(result.items())
print(result_lst)
result_lst.sort(key=lambda x:-x[1]) 
print(result_lst) # 리스트 중 (수지: ) 쌍이 가장 처음 나열. 
print(result_lst[0][0]) #그중 제일 처음 value값으로 검색시 수지 나옴. 
print(result)
print('수지가 반장이 되었습니다')