# 통계_기본
# 컨테이너 자료형 

score = [85,90,78,95,88]
print(score)

#1.평균구하기
print(sum(score)/len(score))

#2.중앙값 구하기 
# 리스트 정렬하기 
# 내장함수 sorted -> 정렬이 완료된 새 리스트 반환 
# 리스트 메서드 sort() -> 기존 리스트 변경 

score.sort()
print(score[2]) #인덱스로 중앙값 지정 or 전체 데이터 짝/홀수 수에 따른 함수(추후)

#3. 최빈값
# 딕셔너리 생성해 갯수세기 
# 동일 갯수일 경우, 최빈값 구할 수 없다 

score_cnt={}

for n in score:
    if n not in score_cnt:
        score_cnt[n] = 1
    else:
        score_cnt[n] += 1 

print(score_cnt)

#4. 범위(Range)

score_range = max(score)-min(score) # 방법1 : 연산 
print(score_range) 
print(score[-1]-score[0]) # 방법2 : 이미 정렬되었으니, 인덱싱 활용 
