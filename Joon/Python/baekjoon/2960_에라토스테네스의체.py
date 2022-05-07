from math import sqrt


N, K = map(int,input().split())

numbers = [True for _ in range(N+1)]
arr = []

for i in range(2,N+1):
      if numbers[i]:
          j = 1
          while i * j <= N:
                if numbers[i*j]:
                  numbers[i*j] = False
                  arr.append(i*j)
                j+=1

print(arr[K-1])