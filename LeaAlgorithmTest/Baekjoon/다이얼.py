

nums = input()
time = 0

for i in nums:
    if i in ['A','B','C']:
        time += 3 #숫자 1은 2초, 1보다 큰수는 1초씩 더 걸림
    elif i in ['D', 'E', 'F']:
        time += 4
    elif i in ['G', 'H', 'I']:
        time += 5
    elif i in ['J', 'K', 'L']:
        time += 6
    elif i in ['M', 'N', 'O']:
        time += 7
    elif i in ['P', 'Q', 'R', 'S']:
        time += 8
    elif i in ['T', 'U', 'V']:
        time += 9
    elif i in ['W', 'X', 'Y', 'Z']:
        time += 10

print(time)

