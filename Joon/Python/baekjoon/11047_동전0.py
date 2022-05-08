N, K = map(int,input().split())
won = [0] * N;

for i in range(N-1,-1,-1):
    won[i] = int(input())

count = 0
for j in won:
    if K >= j:
        count += K // j
        K -= K // j * j

print(count)