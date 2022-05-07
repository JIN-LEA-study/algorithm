from collections import deque
n = int(input())
numbers = list(map(int,input().split()));
stack = deque()
result = [-1 for _ in range(n)]
for i in range(n):
    while stack and (numbers[stack[-1]] < numbers[i]):
        idx = stack.pop()
        result[idx] = numbers[i];
    stack.append(i)

while stack:
    result[stack.pop()] = -1

print(*result)
