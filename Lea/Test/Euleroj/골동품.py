'''
골동품

경매에 굉장히 좋은 골동품이 나왔다. 골동품을 입찰받기 위해서는 흥정을 하게 되는데, 맨 처음 내가 제시한 가격을 A, 판매사가 제시한 가격을 C라고 하자. 만일 A와 C가 같다면 이 가격에 골동품을 입찰받게 되지만 그런 경우는 흔치 않고, 매번 입찰할 때마다 내가 제시한 가격은 B씩 올라가며, 이에 대해 판매사는 D씩 내려간다. 가격이 결정되는 순간은 두 가격이 같거나, 내가 제시한 가격이 입찰자가 제시하는 가격보다 클 두 경우 모두 내가 제시한 가격에 골동품을 입찰받게 된다. 골동품의 가격을 결정하는 프로그램을 작성하여라.

'''

# a = 내가 제시한 가격
# c = 판매사가 제시한 가격
# b = 입찰 할 때마다 내가 제시한 가격은 B씩 올라감
# d = 판매사는 D씩 내려감

# 가격이 결정되면 두 가격이 같거나, 내가 제시한 가격이 입찰자 제시 가격보다 클 경우 모두 내가 제시한 가격에 골동품 입찰


a,b,c,d = map(int, input().split())

while a < c :
    a += b
    c -= d
print(a)

