'''
[Question 4] = (40점, 부분점수 있음)
다른 추천 동영상 목록 API 데이터 videos와 본인의 실제 시청 기록 views 데이터가 주어질 때 다음 질문에 답하시오.
단, 비디오의 장르(카테고리)는 1~5까지의 자연수만 있다고 가정한다.

(1) 추천 동영상 목록 videos에서 몇 개의 동영상 데이터를 응답 받았는지 구하시오. (동영상 정보는 results) (10점)
(2) 내가 시청한 동영상(views)들의 평점의 평균을 구하시오. (10점)
(3) 내가 시청한 동영상(views)들 중 가장 많이 시청한 장르를 구하시오. (10점)
(4) 내가 가장 많이 시청한 장르 중 추천 비디오 데이터 베이스에서 평점이 가장 높은 동영상의 제목을 출력하시오. (10점)
'''

# 추천 동영상 목록
videos = {
    'response': 'Success',
    'current_page': 1,
    'results': [
        {'title': '갑', 'video_genre': 2, 'rating': 1.423},
        {'title': '을', 'video_genre': 3, 'rating': 5.225},
        {'title': '병', 'video_genre': 1, 'rating': 6.814},
        {'title': '정', 'video_genre': 2, 'rating': 7.137},
        {'title': '무', 'video_genre': 2, 'rating': 5.576},
        {'title': '기', 'video_genre': 3, 'rating': 6.754},
        {'title': '경', 'video_genre': 1, 'rating': 8.339},
        {'title': '신', 'video_genre': 3, 'rating': 9.127},
        {'title': '임', 'video_genre': 2, 'rating': 8.934},
        {'title': '계', 'video_genre': 1, 'rating': 5.147},
        {'title': '자', 'video_genre': 2, 'rating': 2.996},
        {'title': '축', 'video_genre': 2, 'rating': 3.842},
        {'title': '인', 'video_genre': 2, 'rating': 7.123},
        {'title': '묘', 'video_genre': 5, 'rating': 5.465},
        {'title': '진', 'video_genre': 2, 'rating': 8.846},
        {'title': '사', 'video_genre': 4, 'rating': 3.157},
        {'title': '오', 'video_genre': 3, 'rating': 8.752},
        {'title': '미', 'video_genre': 4, 'rating': 6.936},
        {'title': '신', 'video_genre': 2, 'rating': 9.998},
        {'title': '유', 'video_genre': 2, 'rating': 5.246},
        {'title': '술', 'video_genre': 2, 'rating': 2.502},
        {'title': '해', 'video_genre': 3, 'rating': 4.478},
    ]
}

# 내 시청기록 (title 제외)
views = [
    {'video_genre': 1, 'rating': 7.226},
    {'video_genre': 3, 'rating': 2.442},
    {'video_genre': 2, 'rating': 8.683},
    {'video_genre': 2, 'rating': 9.676},
    {'video_genre': 3, 'rating': 4.213},
    {'video_genre': 2, 'rating': 3.724},
    {'video_genre': 2, 'rating': 5.553},
    {'video_genre': 4, 'rating': 9.155},
    {'video_genre': 3, 'rating': 4.667},
    {'video_genre': 5, 'rating': 5.972},
    {'video_genre': 5, 'rating': 6.374},
    {'video_genre': 1, 'rating': 3.826},
    {'video_genre': 2, 'rating': 1.732},
    {'video_genre': 1, 'rating': 7.945},
    {'video_genre': 2, 'rating': 1.337},
]
# 정답 
# 1번 풀이 : 딕셔너리 내 리스트 = 내답 
print(videos['results']) #type, 컨테이너 자료형 list
print(len(videos['results']))


# 2번 풀이 : 리스트 내 딕셔너리 (**헷갈린다. for문으로 각 요소 불러와도) (for문,딕셔너리 변수지정)
# 평균 = 합산 / 개수 

total_rating = 0  # 합산값 초기화 
cnt = 0 # 내가 본 영화 수 초기화 

for view in views:
    total_rating += view['rating'] #재할당, print로 확인하면서 조정, #반복하며, 평점합산(분자)
    cnt += 1 # 반복하며, 분모 1씩 증가 (분모)
print(total_rating/cnt)


# 3번 풀이 : 딕셔너리 등급별 갯수 세기 (**헷갈린다. 반장문제와 같은데 왜 계속 틀리지)

most_genre = {1:0,2:0,3:0,4:0,5:0} # 등급 1-5사이니, 간편히 미리 구성 

for view in views:
    most_genre[view['video genre']]+=1 # 딕셔너리[키값=변수[인덱스]] 구조 이해
print(most_genre)


for genre in most_genre:
    if most_genre[genre] == max(most_genre.values()): # for, if 문 변수정리 필요  
        favorite_genre = genre 
        break # 돌리지말고 하나만 뽑으면 끝 
print(favorite_genre)

# 4번 풀이 : 3번과 연계 
# 방법 1) 

recommended = []

for video in videos ['results']:
    if video['video_genre'] == favorite_genre:
        title = video['title']
        rating = video['rating']
        
        recommended.append([title,rating]) or #
        recommended.append([video['title'],video['rating']]) # 이경우, 위 title, rating 변수 안지정해도 됨 

answer=sorted(recommended, key=lambda x:-x[1]) #sorted로 정렬, 반환하는 내장함수니 answer로 
print(answer[0][0])

# 방법 2) 최대값, 최소값 갱신방식 

# 내답


print(len(videos['results']))

# 2번 풀이

rating = []

for i in views:
    if i['rating']:
        rating.append(i['rating'])

average=sum(rating)/len(rating)
print(round(average,2))

# 3번 풀이

genre={}

for n in views:
    if n['video_genre'] not in genre:
        genre[n['video_genre']]=1
    else:
        genre[n['video_genre']]+=1

print(genre)
sorted(genre, key=lambda x:-[x])

# 4번 풀이

