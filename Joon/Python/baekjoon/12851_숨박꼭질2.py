from collections import deque

MAX_SIZE = 1000001
cnt = 0
def bfs(start,end,visited):
    global cnt;
    queue = deque([start])
    while queue:
        v = queue.popleft()
        if v == end:
           cnt+=1
        for i in [v-1,v+1,v*2]:
            if 0<=i<MAX_SIZE:
                if visited[i] == -1 or visited[i]==visited[v]+1:
                    visited[i] = visited[v]+1
                    queue.append(i)            

n,k = map(int,input().split())
visited = [-1] * MAX_SIZE
visited[n] = 0
bfs(n,k,visited)
print(visited[k],cnt,sep="\n")