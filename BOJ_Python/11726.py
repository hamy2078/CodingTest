N = int(input())

tiles = [[0]]*(N+3)
tiles[1] = [1]
tiles[2] = [2]
for i in range(3,N+1):
    tiles[i] = [tiles[i-1][0]+tiles[i-2][0]]

print(tiles[N][0]%10007)
