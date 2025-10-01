# 문제: 다음 온도 데이터(섭씨)를 화씨로 변환한 리스트를 생성하고,
# 섭씨 온도 기준 구간별로 분류한 리스트를 생성하세요. (추위: <10, 보통: 10-25, 더위: >25)

celsius_temps = [5, 15, 22, 30, 8, 18, 35, 12, 28, 3]

# 섭씨-화씨 변환 공식 : 화씨 = (섭씨 × 9/5) + 32
# for문을 사용해서 각 온도를 화씨로 변환하고, if문을 사용해서 온도를 구간별로 분류하세요.
# 해답 코드

# 빈 리스트 두 개를 만들어서 화씨 온도와 온도 분류를 저장
fahrenheit_temps = []
temp_categories = []

# for문으로 celsius_temps의 각 온도를 순회
for celsius in celsius_temps:
    # 각 온도에 대해 화씨 변환 공식을 적용
    fahrenheit = (celsius * 9/5) + 32
    fahrenheit_temps.append(fahrenheit)
    
    # if-elif-else문을 사용해서 섭씨 온도를 기준으로 구간별로 분류
    if celsius < 10:
        category = '추위'
    elif celsius <= 25:
        category = '보통'
    else:
        category = '더위'
    
    temp_categories.append(category)

print(f"화씨 온도: {fahrenheit_temps}")
print(f"온도 분류: {temp_categories}")

# 출력 예시
# 화씨 온도: [41.0, 59.0, 71.6, 86.0, 46.4, 64.4, 95.0, 53.6, 82.4, 37.4]
# 온도 분류: ['추위', '보통', '보통', '더위', '추위', '보통', '더위', '보통', '더위', '추위']