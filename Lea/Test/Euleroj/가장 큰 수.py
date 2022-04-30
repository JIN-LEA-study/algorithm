

num,n=map(int,input().split())
num=list(map(int,str(num)))

stack=[]

for x in num:
    while n>0:
        if len(stack)==0:
            break
        elif stack[-1]<x:
            stack.pop()
            n-=1
        else:
            break
    stack.append(x)

if n>0:
    stack=stack[:-n]

print(''.join(map(str,stack)))



# num, m = map(int, input().split()) #정수, 띄어쓰기로 받기
# num = list(map(int, str(num))) #num을 list로 만들어주기, str 처리해주기.
# stack = [] #빈리스트 만들어주기

# for x in num:
#     while stack and m > 0 and stack[-1] < x: #stack이 비워져있지 않고,  -1 맨 마지막 인덱스
#         stack.pop()
#         m -= 1 #m의 갯수 마이너스
#     stack.append(x)
# if m!=0:
#     stack=stack[:-m]
# for x in stack:
#     print(x, end='') #join해서 붙여서 출력해주기










