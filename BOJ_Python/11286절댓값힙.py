import sys
import heapq

# 큐에 기준이 두가지
# 1. 절댓값이 가장 작은 수
# 2. 절댓값이 가장 작은 값이 여러개 일 때는, 가장 작은 수
abs_q = []
n = int(sys.stdin.readline())
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        try:
            sys.stdout.write(str(heapq.heappop(abs_q)[1])+'\n')
        except:
            sys.stdout.write(str(0)+'\n')
    else:
        heapq.heappush(abs_q,[abs(x),x])
        
