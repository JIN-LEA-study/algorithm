
# #1부터 N까지 출력하기

# n = int(input())
# for i in range(1, n+1):
#     print(i)

# # 1부터 N까지 홀수 출력

# n = int(input())
# for i in range(1, n+1):
#     if i%2==1:
#         print(i)

# # 1부터 N까지의 합을 구하기

# n=int(input())
# sum=0 #합을 담아줄 변수
# for i in range(1, n+1):
#     sum=sum+i
# print(sum) #모든 for문이 끝나고 마지막 모든 합이 담긴 값만 출력


# N의 약수 출력
# 어떤 정수를 나누어 떨어지게 하는 0이 아닌 정수

n=int(input())
for i in range(1, n+1):
    if n%i==0:
        print(i, end=' ') #옆으로 출력


