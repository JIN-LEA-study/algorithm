
#2차원 리스트 생성과 접근

a=[0]*3 #크기가 3인 list 생성(1차원)
print(a)

a=[[0]*3 for _ in range(3)]
print(a) #[[0, 0, 0], [0, 0, 0], [0, 0, 0]]

a[0][1]=1
print(a) #[[0, 1, 0], [0, 0, 0], [0, 0, 0]]
print(a[0][1]) #1

a[1][1]=2
print(a) #[[0, 1, 0], [0, 2, 0], [0, 0, 0]]

for x in a:
    print(x, sep=",", end=" ")
print()

#이중for문
for x in a:
    for y in x:
        print(y, end=" ")
    print()



