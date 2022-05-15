N, M = map(int,input().split())
arr = {}
for i in range(N):
    arr[input()] = 1

count = 0
for i in range(M):
    try:
        if arr[input()]:
            count+=1
    except:
        continue;

print(count)

#set을 사용하는 방법
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# s = set([input() for _ in range(N)])
# cnt = 0
# for _ in range(M):
#     t = input()
#     if t in s:
#         cnt += 1
# print(cnt)