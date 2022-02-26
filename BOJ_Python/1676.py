import math

n = int(input())
fac = math.factorial(n)

cnt = 0
while True:
    rest = fac%10
    fac = fac // 10
    if rest == 0:
        cnt+=1
    else: break

print(cnt)
