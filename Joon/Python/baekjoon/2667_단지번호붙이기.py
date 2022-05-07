from collections import deque
import sys
input = sys.stdin.readline

N = int(input());
graph = [ list(map(int,input().strip())) for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
house = []


def bfs(a,b):
    queue = deque()
    queue.append([a,b])
    graph[a][b] = 0;
    cnt = 1

    while queue:
        x, y = queue.popleft();
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny]=0
                queue.append([nx,ny])
                cnt += 1
    return cnt

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            house.append(bfs(i,j))


print(len(house))
house.sort();
print(*house,sep="\n");