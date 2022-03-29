
#함수만들기

def add(a, b):
    c=a+b
    print(c)
add(3, 2) #5 함수호출, 함수를 작동시켜라~
add(5, 7) #12

#예시1
def add(a, b):
    c=a+b
    return c
print(add(3, 2))

#예시2
def add(a, b):
    c=a+b
    return c #함수를 종료하는 역할
x=add(3, 2)
print(x)

#예시3

def add(a, b):
    c=a+b
    d=a-b
    return c, d
print(add(3, 2))

#예시4 소수만 찾아내는 함수 만들기
#소수 1과 자기자신만 나누어 떨어지는 1보다 큰 정수

def isPrime(x):
    for i in range(2, x):
        if x%i == 0:
            return False
    return True


a = [12, 13, 7, 9, 19]

for y in a:
    if isPrime(y):
        print(y, end=" ") #13, 7, 19 소수만 출력