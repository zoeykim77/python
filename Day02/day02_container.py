#컨테이너 특성
#순서 o, x
#변경 0,x

#형 변환
#문자열 -> 리스트 변경
#각 문자가 개별 원소로 바뀌고, '순서o' '변경o' 리스트가 된다. 
word = 'python'
word_lst = list(word)
print(word_lst)

# range -> 리스트 
number_range = range(10)
number_lst = list(number_range) #열로 세로로아닌, 가로로 나열됨 

#str,tuple -> ???할 순 있지만, 사용시 주의 기울여야 한다. 공백도 레인지처리함. ??
str_number = str(number_lst)
print(str_number)
print(str_number[3]) #대괄호나 콤파, 공백조차 문자열 인식