

'''
크게만들기

N자리 숫자가 주어졌을 때, 여기서 숫자 K개를 지워서 얻을 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.

입력

첫째 줄에 N과 K가 주어진다. (1 ≤ K < N ≤ 500,000)
둘째 줄에 N자리 숫자가 주어진다. 이 수는 0으로 시작하지 않는다.

출력

입력으로 주어진 숫자에서 K개를 지웠을 때 얻을 수 있는 가장 큰 수를 출력한다.

'''

n, k = map(int, input().split()) #정수로 입력받기
number = list(input()) #리스트로 입력받기

ans = []
cnt = k
for num in number:
    while ans and cnt > 0 and ans[-1] < num:
        del ans[-1]
        cnt -=1
    ans.append(num)
print(''.join(ans[:n-k]))
