


'''
A+b - 3

두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

각 테스트 케이스마다 A+B를 출력한다
'''

# T = int(input())
# a = []

# for i in range(T): #입력받은 T의 갯수만큼 테스트
#     a, b = map(int, input().split()) #a, b 한줄로 입력받기
#     sum = a+b
#     a.append(sum)
#     for i in a:
#         print(a)



T = int(input())

for i in range(T): #입력받은 T의 갯수만큼 테스트
    a, b = map(int, input().split()) #a, b 한줄로 입력받기
    print(a+b)




