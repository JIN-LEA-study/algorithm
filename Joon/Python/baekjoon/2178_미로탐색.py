from collections import deque
import sys

def bfs(a,b):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    queue = deque()
    queue.append([a,b])
    
    
    while queue:
        x,y = queue.popleft()
        if y == (M-1) and x == (N-1):
            print(visited[x][y])
            break
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx,ny])
                    graph[nx][ny] = 0
                
input = sys.stdin.readline;
N,M = map(int,input().strip().split())

graph = [[0] for _ in range(N)]
visited = [[0] * M for _ in range(N)]


for i in range(N):
    graph[i] = list(map(int,input().strip()))


visited[0][0] = 1;
bfs(0,0)
