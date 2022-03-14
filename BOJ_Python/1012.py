# DFS
import sys
sys.setrecursionlimit(3000) # 재귀 깊이 제한

def dfs(x,y):
    # 좌표가 범위를 벗어난 경우 즉시 종료
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False
    # 현재 노드를 방문한 적이 없다면
    if graph[y][x] == 1:
        
        graph[y][x] = 0

        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

T = int(input())

for _ in range(T):
    m,n,k = map(int,input().split())
    graph = [[0]*m for i in range(n)]
    for _ in range(k):
        x,y = map(int,input().split())
        graph[y][x] = 1
    cnt = 0
    for i in range(m):
        for j in range(n):
            if dfs(i,j) == True:
                cnt += 1
    print(cnt)

