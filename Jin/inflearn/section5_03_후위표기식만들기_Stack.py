'''
후위표기식 만들기(infix to postfix)

중위표기식이 입력되면 후위표기식으로 변환하는 프로그램을 작성하세요.
중위표기식은 우리가 흔히 쓰은 표현식입니다. 즉 3+5 와 같이 연산자가 피연산자 사이에 있으면 중위표기식입니다.
후위표기식은 35+ 와 같이 연산자가 피연산자 뒤에 있는 표기식입니다.
예를 들어 중위표기식이 3+5*2 를 후위표기식으로 표현하면 352*+ 로 표현됩니다.
만약 다음과 같이 연산 최우선인 괄호가 표현된 식이라면 (3+5)*2 이면 35+2* 로 바꾸어야 합니다.

※후위 표기식이 이해가 안되면 구글링으로 공부해보는 것도 좋습니다.

- 입력설명
첫 줄에 중위표기식이 주어진다. 길이는 100을 넘지 않는다.
식은 1~9의 숫자와 +, -, *, /, (, ) 연산자로만 이루어진다.

- 출력설명
후위표기식을 출력한다.

- 입력예제 1
3+5*2/(7-2)

- 출력예제 1
352*72-/+

- 입력예제 2
3*(5+2)-9

- 출력예제 2
352+*9-
'''

# 우선순위가 같다면 stack에 있는게 더 우선(왼쪽에 있는 자료이기 때문에)
# 여는 괄호는 무조건 append
# 여는 괄호는 닫는 괄호를 만났을 때 꺼낸다.

a = input()
stack = []
res = ''  # 누적 예정  # 출력을 res에

for x in a:  # 중위식을 하나하나 문자 탐색하는 것이 x이다.
    if x.isdecimal():  # 숫자인지를 봐야 한다 # 십진수 숫자이면 참
        res += x  # 그대로 출력 # res를 출력이라고 할 예정
    else:
        if x == '(':
            stack.append(x)  # 여는 괄호는 무조건 append
        elif x == '*' or x == '/':  # 연산 우선순위가 빠른 애들만 stack에서 꺼내는 것
            while stack and (stack[-1] == '*' or stack[-1] == '/'):  # [-1] 스택의 가장 상단 가장 최근 자료 가장 뒷자료 # 이런 자료는 stack에서 먼저 꺼내 처리
                res += stack.pop()  # stack의 가장 상단의 자료가 pop되어 res에 누적  # 출력했다고 생각하기
            stack.append(x)
        elif x == '+' or x == '-':  # stack에 있는 +-는 자기에 있는 것보다 다 빠름  # 더 왼쪽 자료이기 떄문
            while stack and stack[-1] != '(':  # 여는 괄호 전까지만 # 여는 괄호 만나면 멈춰야한다.
                res += stack.pop()
            stack.append(x)
        elif x == ')':  # 닫는 괄호를 만났다.
            while stack and stack[-1] != '(':  # 여는 괄호까지 간다.
                res += stack.pop()  # 여기는 빼는 것
            stack.pop()  # 여는 괄호를 끄집어 낸다. 출력 안하고 없애버린다.

while stack:
    res += stack.pop()  # 남아 있는 것들 pop하면서 출력

print(res)
