
from collections import deque

def bfs(x):
    cnt = 0

    visited = [False]*(m+1)
    visited[0] = True
    
    queue = deque()
    queue.append(x)
    visited[x] = True
    
    while queue:
        x = queue.popleft()
        cnt += 1
        for i in graph[x]:
            if visited[i] == False: # 이전에 방문한 적이 없다면.
                visited[i] = True
                queue.append(i)
        
    return cnt-1

m = int(input())
edge = int(input())

graph = [[]for i in range(m+1)]

for _ in range(edge):
    v1, v2 = map(int,input().split())
    # 양방향 연결
    graph[v1].append(v2)
    graph[v2].append(v1)
    
print(bfs(1))
