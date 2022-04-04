'''
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
'''

star = int(input())

for i in range(1, star+1): #star 갯수만큼 for문으로 반복
    print('*' * i) #별을 i가 돌면서 곱해주기
