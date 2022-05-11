
from collections import deque


def bfs(start,end,visited):
    visited[start] = 1
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for i in [v*10+1,v*2]:
            if(i <= end and not visited.get(i)):
                visited[i] = visited[v] + 1
                if i == end: 
                    return
                else:
                    queue.append(i)
                
                
                

A,B = map(int,input().split())
visited = {}
bfs(A,B,visited)
print(visited[B] if visited.get(B) else - 1)