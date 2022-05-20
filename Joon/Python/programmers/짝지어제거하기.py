def solution(s):
    stack = []
    
    for x in s:
        if stack:
            if stack[-1] == x:
                stack.pop()
            else:
                stack.append(x)
        else:
            stack.append(x)        
    return 1 if not stack else 0