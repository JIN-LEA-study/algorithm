
'''
팩토리얼 #10872

0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

'''

n = int(input())
sum = 1 #1부터
for i in range(1, n+1):
    sum *= i #1*1, 1*2 ..

print(sum)



# 팩토리얼 재귀 함수식으로 풀기

def factorial(n):
    result = 1
    if n > 0 : #0일 경우 그냥 result는 1
        result = n * factorial(n-1)
    return result

n = int(input())
print(factorial(n))


def factorial2(n):
    if n == 0:
        return 1
    return n * factorial2(n-1)

n = int(input())
print(factorial2(n))

