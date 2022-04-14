
'''
팩토리얼 #10872

0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

'''

n = int(input())
sum = 1 #1부터
for i in range(1, n+1):
    sum *= i #1*1, 1*2 ..

print(sum)

