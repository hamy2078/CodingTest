import sys

N = int(sys.stdin.readline())

tiles = [1,2,-1]

for i in range(3,N+1):
    # 결과값만 나눠주는 것이 아니라 중간에 연산을 해줘야 시간초과나 메모리 초과가 발생하지
    # 않는다.
    tiles[2] = (tiles[0] + tiles[1])%15746 
    tiles[0] = tiles[1]
    tiles[1] = tiles[2]
if N == 1:
    sys.stdout.write(str(tiles[0]))
elif N == 2:
    sys.stdout.write(str(tiles[1]))
else:
    sys.stdout.write(str(tiles[2]))
