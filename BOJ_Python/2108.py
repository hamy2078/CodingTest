import math
import sys
from collections import Counter

n = int(sys.stdin.readline())

num = []
for _ in range(n):
    num.append(int(sys.stdin.readline()))
num.sort()

mean = sum(num)/n
if mean > 0:sys.stdout.write(str(int(mean+0.5))+'\n')
else:sys.stdout.write(str(int(mean-0.5))+'\n')
    
sys.stdout.write(str(num[math.floor(n/2)])+'\n')

cnt = Counter(num).most_common()# 데이터의 개수가 많은 순으로 정렬된 배열을 리턴, most_common
if len(cnt) == 1 or cnt[0][1]!=cnt[1][1]:
    print(cnt[0][0])
else:
    print(cnt[1][0])
    
sys.stdout.write(str(num[-1]-num[0])+'\n')
