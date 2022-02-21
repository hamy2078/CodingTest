t = int(input())

for i in range(t):
    h,w,n = map(int, input().split())
    rest = n%h
    share = n//h
    if rest == 0:
        rest = h
        share -= 1
    print(rest*100+share+1)
