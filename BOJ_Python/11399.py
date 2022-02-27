import sys
import itertools

n = int(sys.stdin.readline())
minute = list(map(int,sys.stdin.readline().split()))
minute.sort()

wait = []
for i in range(n):
    wait.append(sum(minute[:i+1]))
print(sum(wait))
