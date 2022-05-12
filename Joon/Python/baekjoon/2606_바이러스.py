def dfs(graph,v,visited):
    global cnt;
    visited[v] = 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

n = int(input())
m = int(input())

visited = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for i in range(m):
    start, end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start) 

dfs(graph,1,visited)
print(sum(visited) - 1)