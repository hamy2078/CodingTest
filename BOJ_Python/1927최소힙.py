import sys
import heapq

min_q = []
n = int(sys.stdin.readline())
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        try:
            sys.stdout.write(str(heapq.heappop(min_q))+'\n')
        except:
            sys.stdout.write(str(0)+'\n')
    else:
        heapq.heappush(min_q,x)
        
