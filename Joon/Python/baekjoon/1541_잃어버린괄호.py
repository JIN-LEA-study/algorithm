import sys
input = sys.stdin.readline

sik = input()
stack = ''
arr = []
plus_minus = True

for x in sik:
    if x == '+':
        arr.append(int(stack) * (1 if plus_minus else -1 ))
        stack = ''
    elif x == '-':
        arr.append(int(stack) * (1 if plus_minus else -1))
        plus_minus = False
        stack = ''
    else:
        stack += x

if stack:
    arr.append(int(stack) * (1 if plus_minus else -1 ))
    stack = ''

print(sum(arr))