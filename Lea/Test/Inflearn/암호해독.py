
'''

문제1. 암호해독

모든 알고리즘을 해독할 수 있는 알고리즘 7 원석를 보유한 알고리즘 제왕 파이와 썬은 죽기 전, 이 보물에 '암호'를 걸어 세계 어딘가에 묻어놨다고 공표하였다. 그가 남긴 문자는 아래와 같다.

섬으로 향하라!

'   + -- + - + -   '
'   + --- + - +   '
'   + -- + - + -   '
'   + - + - + - +   '

해(1)와 달(0),
Code의 세상 안으로!(En-Coding)

'''



text = ['   + -- + - + -   ',
'   + --- + - +   ',
'   + -- + - + -   ',
'   + - + - + - +   ']


for i in text:
    print(int(i.strip().replace(' ', '').replace('+', '1').replace('-', '0'), 2))

#ord 문자 -> 숫자
#chr 숫자 -> 문자

for i in text:
    print(chr(int(i.strip().replace(' ', '').replace('+', '1').replace('-', '0'), 2)))

L=[]
for i in text:
    L.append(chr(int(i.strip().replace(' ', '').replace('+', '1').replace('-', '0'), 2)))

print(''.join(L))

#Join알아보기 char array to string










'''

strip() 양쪽 끝에 있는 공백 제거

replace()
replace(old, new, [count])
old 현재 문자열에서 변경하고 싶은 문자
new 새로 바꿀 문자
count 변경할 횟수, 입력하지 않으면 old 문자열 전체를 바꿈
'oxoxox'.replace('ox', '*', 1)
*oxox

'''

