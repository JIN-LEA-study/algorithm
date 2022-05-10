import sys

def reverse(string):
    result = ""
    stack = []
    for char in string:
        stack.append(char)
    
    for i in range(len(string)):
        result += stack.pop()
    
    return result
n = int(sys.stdin.readline())

for i in range(n):
    result = []
    input = sys.stdin.readline().strip().split();
    for i in range(len(input)):
        result.append(reverse(input[i]))
    print(" ".join(result))


