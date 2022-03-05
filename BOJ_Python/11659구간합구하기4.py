import sys
n, m = map(int,sys.stdin.readline().split())
number = list(map(int,sys.stdin.readline().split()))
# 자주 사용되는 데이터는 미리 계산해두면 시간을 절약할 수 있다.
sum_array = [0]
tmp = 0
for i in range(n):
    tmp += number[i]
    sum_array.append(tmp)

for _ in range(m):
    i, j = map(int,sys.stdin.readline().split())
    sys.stdout.write(str(sum_array[j]-sum_array[i-1])+'\n')
