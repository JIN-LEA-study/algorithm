import sys
input = sys.stdin.readline
In = list(input().strip())
count = 0
while True:
    In = sum(list(map(int,In)))
    count += 1
    if In < 10:
        break;
    In = list(str(In))
print(count)
if In == 3 or In == 6 or In == 9:
    print("YES")
else:
    print("NO")