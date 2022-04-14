
#람다함수 (익명의 함수)

#일반함수
def plus_one(x):
    return x+1
print(plus_one(1)) #1

#람다함수
plus_two=lambda x: x+2
print(plus_two(1)) #3

#유용한 경우(표현식)

def plus_one(x):
    return x+1

a=[1, 2, 3]
print(list(map(plus_one, a))) #map은 인자가 2개, (함수명, a라는 리스트에 작동) #[2, 3, 4]
print(list(map(lambda x: x+1, a))) #[2, 3, 4]

