from collections import deque


def bfs(start,end,visited):
    if start==end:
        return
    visited[start] = 0
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for i in [v-1,v+1,v*2]:
            if 0<=i<=100000 and not visited[i] and i != start:
                visited[i] = visited[v] + 1
                queue.append(i)


n,k = map(int,input().split())
visited = [0] * 100001
bfs(n,k,visited)
print(visited[k])
