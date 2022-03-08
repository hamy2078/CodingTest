import sys

N = int(sys.stdin.readline())

house = [[0,0,0]]
house.append(list(map(int,sys.stdin.readline().split())))

for i in range(2, N+1):
    price = list(map(int,sys.stdin.readline().split()))
    price = [price[0] + min(house[i-1][1],house[i-1][2]),
     price[1] + min(house[i-1][0],house[i-1][2]),
     price[2] + min(house[i-1][0],house[i-1][1])]
    house.append(price)

sys.stdout.write(str(min(house[N])))
