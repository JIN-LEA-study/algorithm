
#중첩 반복문 (이중for문)

for i in range(5):
    for j in range(5):
        print(j, end=" ")
    print() #줄바꿈

for i in range(5):
    print('i:', i, sep="", end=" ")
    for j in range(5):
        print('j:', j, sep="", end=" ")
    print()

for i in ragne(5):
    for j in range(5):
        print('*', end= ' ')
    print()

for i in range(5):
    for j in range(i+1):
        print('*', end=' ')
    print()


for i in range(5):
    for j in range(5-i):
        print("*", end=" ")
    print()