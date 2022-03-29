
#변수입력과 연산자

a=input('숫자를 입력해주세요 : ') #input은 입력값을 받을 수 있음
print(a)

a,b =input('숫자를 입력해주세요:').split() #split은 입력값을 띄어쓰기로 구분해준다. 문자열로 받는다.
print(a+b) #23
print(type(a)) #str

a,b =input('숫자를 입력해주세요: ').split()
a = int(a) #문자열을 str로 변환
print(type(a)) #int
print(type(b)) #str

b = int(b)
print(type(b)) #int

a, b =map(int, input('숫자를 입력해주세요: ').split()) #한꺼번에 int로 변환을 하고 싶을 땐 map 함수를 써준다.
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) #몫
print(a%b) #나머지
print(a**b) #거듭제곱

#type이 실수+정수일 경우 실수형 (연산결과는 더 큰 범위가 나온다)




