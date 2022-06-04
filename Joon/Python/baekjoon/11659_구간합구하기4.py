import sys
input = sys.stdin.readline
N, M = map(int,input().strip().split());
arr = list(map(int,input().split()))

for _ in range(M):
    i, j = map(int,input().strip().split());
    print(sum(arr[i-1:j]))