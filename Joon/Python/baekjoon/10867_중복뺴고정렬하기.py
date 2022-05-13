N = int(input())

result = set(map(int,input().split()))
result = sorted(list(result));
print(*result);