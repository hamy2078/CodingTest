import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    k = int(sys.stdin.readline())
    base = [i+1 for i in range(k)]
 
    for _ in range(n):
        next_floor = [sum(base[:kidx+1])for kidx in range(k)]
        base = next_floor
    print(next_floor[k-1])
