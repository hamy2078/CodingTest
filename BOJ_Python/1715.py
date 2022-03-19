import heapq
import sys

input = sys.stdin.readline

n = int(input())

min_heap = [] # 최소 힙
for _ in range(n):
    heapq.heappush(min_heap, int(input()))

result = 0
for _ in range(n-1):
    min1 = heapq.heappop(min_heap)
    min2 = heapq.heappop(min_heap)
    result = result + min1 + min2
    heapq.heappush(min_heap,min1+min2)

sys.stdout.write(str(result))
