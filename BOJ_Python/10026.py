from collections import deque

def bfs(x,y,color,cval):

    graph[x][y] = cval
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
                continue
            if graph[nx][ny] == color:
                queue.append((nx,ny))
                graph[nx][ny] = cval
    return True


red = green = blue = 0
red_green = 0

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input()))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            red +=1
            bfs(i,j,'R','RG')
        if graph[i][j] == 'G':
            green +=1
            bfs(i,j,'G','RG')
            
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'RG':
            red_green += 1
            bfs(i,j,'RG',0)
        if graph[i][j] == 'B':
            blue +=1
            bfs(i,j,'B',0)
print(red+green+blue, red_green+blue)
