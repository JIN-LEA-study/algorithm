def gold_bah(n):
    result = []
    for i in range(len(prime)):
        if numbers[n-prime[i]]:
            diff = abs(n-prime[i]-prime[i])
            result.append([diff,prime[i],n-prime[i]])

    result = sorted(result,key=lambda x:x[0]);
    print(result[0][1],result[0][2])
    

T = int(input());

prime = []
numbers = [True for _ in range(10001)]
for i in range(2,10001):
    if numbers[i]:
        prime.append(i);
        j = 2
        while i * j <= 10000:
            numbers[i*j] = False
            j+=1

for i in range(T):
    N = int(input())
    if N % 2 == 1:
        print('짝수가 아닙니다')
        break
    gold_bah(N)


