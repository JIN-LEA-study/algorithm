import sys
input = sys.stdin.readline
N, M = map(int,input().strip().split());
arr = list(map(int,input().split()))
prefix_sum = [0]

temp = 0
for x in arr:
    temp += x
    prefix_sum.append(temp)

for _ in range(M):
    i, j = map(int,input().strip().split());
    print(prefix_sum[j] - prefix_sum[i-1])