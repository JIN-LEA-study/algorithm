import operator
from collections import deque
from functools import reduce

M, N = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
queue = deque([])


res = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append([i,j])

def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx,ny])
bfs()
arr = list(reduce(operator.add,graph))


if arr.count(0):
    print(-1)
else:
    res = max(arr)
    print(res - 1)
