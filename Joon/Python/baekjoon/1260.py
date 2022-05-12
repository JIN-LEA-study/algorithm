from collections import deque


def dfs(graph,v,visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph,start,visited):
    visited[start] = True
    queue = deque([start])
    while queue:
        v = queue.popleft()
        print(v,end=" ")
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

N,M,V = map(int,input().split())

graph = [[] for _ in range(N+1)]
for i in range(M):
    start, end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)
    graph[start].sort();
    graph[end].sort();
    
print(graph)

dfs_visited = [False] * (N+1);
bfs_visited = [False] * (N+1);

dfs(graph,V,dfs_visited)
print()
bfs(graph,V,bfs_visited)