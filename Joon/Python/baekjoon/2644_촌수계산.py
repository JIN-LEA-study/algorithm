from collections import deque

n = int(input())
start, end = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for i in range(m):
    parent, child = map(int,input().split())
    graph[parent].append(child)
    graph[child].append(parent)

visited = [0] * (n+1)
def bfs(start,visited):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = visited[v] + 1
                queue.append(i)
bfs(start,visited)
print(visited[end] if visited[end] else -1)