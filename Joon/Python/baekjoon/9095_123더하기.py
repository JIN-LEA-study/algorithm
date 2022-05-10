T = int(input())
def dp(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    
    if n > 3:
        return dp(n-1) + dp(n-2) + dp(n-3)
for i in range(T):
    print(dp(int(input())))

