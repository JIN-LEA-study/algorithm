
for i in range(1, 6):
    sum = 0
    for j in range(0, i):
        sum = sum + j
    print(sum)


'''
line 3 : i = 1
line 4 : i = 1, sum = 0
line 5 : i = 1, sum = 0, j = 0
line 6 : i = 1, sum = 0, j = 0, sum = 0
line 7 : print(0)

line 3 : i = 2
line 4 : i = 2, sum = 0
line 5 : i = 2, sum = 0, j = 0
lint 6 : i = 2, sum = 0, j = 0, sum = 0
line 5 : i = 2, sum = 0, j = 1
line 6 : i = 2, sum = 0, j = 1, sum = 1
line 7 : print(1)

line 3 : i = 3
line 4 : i = 3, sum = 0
line 5 : i = 3, sum = 0, j = 0
line 6 : i = 3, sum = 0, j = 0, sum 0
line 5 : i = 3, sum = 0, j = 1
line 6 : i = 3, sum = 0, j = 1, sum = 1
line 5 : i = 3, sum = 1. j = 2
line 6 : i = 3, sum = 3
line 7 : print(3)



'''

