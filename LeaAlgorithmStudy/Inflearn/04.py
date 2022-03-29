
#반복문(for, while)

a=range(10)
print(list(a)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

a=range(1, 11) #시작이 1부터 10까지
print(list(a)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(10) :
    print("hello") #hello를 10번 반복
    print(i) #0부터 9까지

for i in range(1, 11) : #1부터 10까지
    print(i)

for i in range(10, 0):
    print(i) #아무 일도 안 일어남

for i in range(10, 0, -1):
    print(i) #-1씩 줄어듦

i=1 #1부터 시작
while i<=10:
    print(i)
    i=i+1 #i에 1씩 더해줌

i=10 #10부터 시작
while i>=1:
    print(i)
    i=i-1 #i에 1씩 w작아짐


#break

i = 1
while True:
    print(i) #1만 무한 반복
    if i == 10:
        break #반복문 멈추기
    i+=1 #i=i+1


#continue

for i in range(1, 11):
    if i&2==0: #짝수
        continue #If문에 해당되는건 스킵
    print(i) #홀수만 출력


#for, else 구문

for i in range(1, 11):
    print(i)
    if i>15:
        break #if문이 돌다가 break에 걸리면 중단, break에 걸리지 않으면 else까지 모두 출력
else:
    print(11) #마지막 11까지 출력