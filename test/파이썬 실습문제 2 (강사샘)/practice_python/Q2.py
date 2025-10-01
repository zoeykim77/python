# 입력된 문자열을 뒤집은 문자열을 구하시오.
# ex) banana 입력 시 ananab 출력

word = input('')
reversed_word=word[::-1]
print(reversed_word)


# 오답 
def reversed_word(word):
    new=list(word).reverse()
    return word

print(reversed_word)

# 로직 작성

string ="banana"
str_lst=list(string)
print(str_lst)

str_lst.reverse()
print(str_lst)

print(str(str_lst))

# print(reversed_word)  # 'banana' 입력 시 reversed_word == 'ananab'