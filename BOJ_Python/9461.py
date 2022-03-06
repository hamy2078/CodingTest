import sys

T = int(sys.stdin.readline())

P = [0]*101

P[1] = P[2] = P[3] = 1
P[4] = P[5] = 2

for i in range(6,101):
    P[i] = P[i-1]+P[i-5]
for _ in range(T):
    N = int(sys.stdin.readline())
    sys.stdout.write(str(P[N])+'\n')
