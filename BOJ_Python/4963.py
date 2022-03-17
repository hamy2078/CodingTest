from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= h or ny <= -1 or ny >= w:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))
                
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,1,-1,-1,0,1]

while True:
    w, h = map(int,input().split())
    if w == 0 and h == 0:break
    
    graph = []
    for _ in range(h):
        graph.append(list(map(int,input().split())))

    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                cnt += 1
                bfs(i,j)
                graph[i][j] = 0
    print(cnt)
