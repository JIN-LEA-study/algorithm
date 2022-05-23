
'''
소수 구하기

M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

'''


# 혼자 풀었지만.. 시간 초과뜸..

m, n = map(int, input().split())

def decimal(x):
  if x == 1:
    return False
  for i in range(2, x):
    if n % i == 0:
      return False
  return True

for i in range(m, n+1):
  if(decimal(i)):
    print(i)




