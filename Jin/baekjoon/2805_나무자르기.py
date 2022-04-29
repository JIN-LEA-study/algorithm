'''
나무 자르기

상근이는 나무 M미터가 필요하다.
목재절단기는 다음과 같이 동작한다.
먼저, 상근이는 절단기에 높이 H를 지정해야 한다.
높이를 지정하면 톱날이 땅으로부터 H미터 위로 올라간다.
그 다음, 한 줄에 연속해있는 나무를 모두 절단해버린다.
따라서, 높이가 H보다 큰 나무는 H 위의 부분이 잘릴 것이고, 낮은 나무는 잘리지 않을 것이다.

예를 들어, 한 줄에 연속해있는 나무의 높이가 20, 15, 10, 17이라고 하자.
상근이가 높이를 15로 지정했다면, 나무를 자른 뒤의 높이는 15, 15, 10, 15가 될 것이고,
상근이는 길이가 5인 나무와 2인 나무를 들고 집에 갈 것이다. (총 7미터를 집에 들고 간다.)
절단기에 설정할 수 있는 높이는 양의 정수 또는 0이다.
이때, 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 나무의 수 N과 상근이가 집으로 가져가려고 하는 나무의 길이 M이 주어진다. (1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000)
둘째 줄에는 나무의 높이가 주어진다. 나무의 높이의 합은 항상 M보다 크거나 같다. 높이는 1,000,000,000보다 작거나 같은 양의 정수 또는 0이다.

출력
적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.

예제 입력 1 
4 7
20 15 10 17

예제 출력 1 
15

예제 입력 2 
5 20
4 42 40 26 46

예제 출력 2 
36
'''

import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, input().split()))

start, end = 0, max(trees)

while start <= end:
    mid = (start + end)//2
    tree = 0
    for i in trees:
        if i > mid:
            tree += i - mid

    if tree >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)
