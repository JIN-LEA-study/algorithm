
#list와 내장함수2

a=[23, 12, 36, 53, 19]
print(a[:3]) #a 안의 0부터 2까지
print(a[1:4]) #1부터 3까지
print(len(a)) #리스트안의 값이 몇개인지? 길이. #5

for i in range(len(a)): #5
    print(a[i], end=" ") #23, 12, 36, 53, 19
print()

for x in a:
    print(x, end=" ") #23, 12, 36, 53, 19
print()

for x in a:
    if x%2==1: #홀수만 출력
        print(x, end=" ")
print()

#enumerate 튜플로 출력 인덱스와 값 같이 출력
#list와 다른점은? 튜플은 값 변경이 불가하다. list는 값 변경이 가능

for x in enumerate(a):
    print(x, end=" ")
print() #(0, 23) (1, 12) (2, 36) (3, 53) (4, 19)

for x in enumerate(a):
    print(x[0], x[1], end=" ") #원소값을 꺼내서 출력
print() #30 23 1 12 2 36 3 53 4 19

# 위랑 똑같이 출력 (원소값을 꺼내서 출력)
for index, value in enumerate(a):
    print(index, value)
print()

# all 모든 조건이 참이여야 출력
if all(60>x for x in a):
    print("yes")
else:
    print("no") #yes

if all(50>x for x in a):
    print("yes")
else:
    print("no") #no

# any 한번이라도 참이면 참, 모든게 거짓일 경우 거짓

if any(12>x for x in a):
    print("yes")
else:
    print("no") #no