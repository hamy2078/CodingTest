def dfs(graph,x,y,num):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    
    if graph[y][x] == 0:
        return False
    else:
        graph[y][x] = 0
        num[0] = num[0] + 1
        dfs(graph,x-1,y,num)
        dfs(graph,x+1,y,num)
        dfs(graph,x,y-1,num)
        dfs(graph,x,y+1,num)
        return True
    return False

n = int(input())
cnt = 0
graph = []
for i in range(n):
    graph.append(list(map(int,list(input()))))

APT = []
for i in range(n):
  for j in range(n):
    num = [0]
    if dfs(graph, i, j,num) == True:
        cnt += 1
        APT.append(num[0])
      
    
print(cnt)
APT.sort()
APT = list(map(str,APT))
APT = '\n'.join(APT)

print(APT)
