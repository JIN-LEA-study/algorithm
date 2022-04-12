

a,b=map(int, input().split())
c=int(input())

h = (a+(b+c)//60)%24 # %24를 안해주면 25시 26시 27시 이런식으로 됨
m = (b+c)%60

print(m)



# a,b = map(int, input().split())
# c=int(input())
# print((a+(b+c)//60)%24, (b+c)%60)




