#11번:
#삼성전자 = 50000
#총평가금액 = 삼성전자 * 10
#print(총평가금액)

#12번:
#시가총액 = 298000000000000
#현재가 = 50000
#PER = 15.79
#print(시가총액, type(시가총액))
#print(현재가, type(현재가))
#print(PER, type(PER))

#13번:
#s = "hello"
#t = "python"
#print(s, "!", t)

#14번:
#>> 2 + 2 * 3

#15번:
#a = "132" / ""나 '로 둘러싸여있으면 걍 문자열임
#print(type(a)) 

###16번:(나한테 중요!)
#num_str = "720" #형 변환
#print(num_str + 1) / 문자열에 숫자를 +할 수 없으니 오류남
#num_int = int(num_str)
#print(num_int+1, type(num_int))

#17번: (16번과 유사문제)
#num = 100
#result = str(num)
#print(result, type(result))

#18번: (역시나 형변환임)
#data = "15.79"
#data = float(data)
#print(data, type(data))

#19번:
#year = "2023"
#print(int(year)-3)
#print(int(year)+3)
#print(year-1) /100% 에러남 문자형으로 되어있기때문.

#20번:
#월 = 48584
#총금액 = 월 * 36
#print(총금액)

#21번:
#letters = "python"
#print(letters[0])
#print(letters[2])

#22번:
#license_plate = "24가 2210" #여기서 공백도 컴퓨터는 샌다.
#print(license_plate[4:8]) #시작과 끝 인덱스 적음
#print(license_plate[4:]) #끝에 숫자안적어줘도 이렇게만 적어도 컴터는 끝으로 인식함
#print(license_plate[-4:]) 

#23번:
#string = "홀짝홀짝홀짝"
#print(string[0:6:2]) #홀0짝1홀2짝3홀4짝5 [0은 시작부분 6은 끝에서(-1)이되기떄문 2는 두칸씩 뛰어넘어가라는거]

#24번:
#string = "PYTHON"
#print(string[::-1]) #뒤집는 표현

#25번~26번:
#phone_number = "010-1111-2222"
#a = phone_number.replace("-"," ") 여기서 빈칸 지우면 번호 붙여서 나옴
#print(phone_number)
#print(a)

#27번:
#url = "http://sharebook.kr" #.을 기점으로 문자열 자르기
#a = url.split(".") #split이 . 을 기점으로 문자열을 나눔
#print(a)
#print(a[1]) # kr만 나오게됨

#28번:
#lang = "pythin"
#lang[0] = 'P'
#print(lang) # TypeError: 'str' object does not support item assignment
#문자열이 python 이 가로가 아닌 세로로 됐을때 0,1,2,3 이렇게 
#p   0
#y   1
#t   2
#o   3
#n   4  으로 되는거. 
#P   가 있는건데 0이 P로 갈 수 없으니 오류가 난다. 

#29번:
#string = "abcdef2a354a32a"
#a = string.replace('a', "A")  # a -> A로 바뀌는걸 프린트하면 확인할 수  있음
#print(a)

#30번:
#string = "abcd"
#string.replace('b', 'B')
#print(string) #해도 바뀌지않음. a =으로 정해줘야함 or string = 
#a = string.replace('b', 'B') == string = string.replace 해도 됨 
#print(a)  a 를 쓰나 string을 쓰나 상관없고 그냥 =이라고 값을 정해주는게 중요함