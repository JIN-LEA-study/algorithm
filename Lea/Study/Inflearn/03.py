
#조건문 if (분기, 중첩)

x=7
if x == 7 : # == 같다, != 같지 않다
    print("lucky") #파이썬에서 들여쓰기는 4칸
    print("ㅋㅋ") #파이썬에서 들여쓰기는 굉장히 중요


# 중첩 if문

x=15
if x >= 10 : #참
    if x%2 == 1: #2나눈 나머지가 1이면 홀수, 0이면 짝수 #참
        print("10이상의 홀수")

x=9
if x > 0 :
    if x<10 : #2나눈 나머지가 1이면 홀수, 0이면 짝수 #참
        print("10보다 작은 자연수")

x=7
if x >0 and x<10 :
    print("10보다 작은 자연수")

x=7
if 0 < x <10 :
    print("10보다 작은 자연수")


#분기문

x=10
if x > 0:
    print("양수") #yes (참)
else:
    print("음수") #no (참이 아니면)



#다중if문

x=93
if x>=90:
    print('A')
elif x>=80:
    print('B')
elif x>=70:
    print('C')
elif x>=60:
    print('D')
else:
    print('F')
