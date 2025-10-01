# 문제: 다음 텍스트 데이터에서 각 단어의 빈도수를 계산하세요.
# 결과를 딕셔너리 형태로 출력하세요.

text_data = "python pandas data analysis visualization machine learning data science python programming"

# 문자열을 특정 문자를 기준으로 분리해서 리스트로 변환하는 방법을 탐색하세요.
# 딕셔너리를 활용해서 리스트의 각 요소를 카운팅하세요.
# 해답 코드
words = text_data.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)

# 출력 예시
# {'python': 2, 'pandas': 1, 'data': 2, 'analysis': 1, 'visualization': 1, 'machine': 1, 'learning': 1, 'science': 1, 'programming': 1} 