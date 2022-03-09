import sys
N = int(sys.stdin.readline())
plan = []
if N < 100:
    sys.stdout.write(str(N))
else:
    cnt = 99
    for i in range(100,N+1): # 최대 999
        a = i // 10 // 10
        b = i // 10 % 10
        c = i % 10
        if a - b == b - c:
            cnt += 1
    sys.stdout.write(str(cnt))

