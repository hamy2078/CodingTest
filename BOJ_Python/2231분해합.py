import sys

n = int(sys.stdin.readline())
st = n - 9 * len(str(n))

if st < 1:
    st = 1
while True:
    m = st + sum([int(i) for i in str(st)])#각 자릿수의 합
    if m == n:
        print(st)
        break  
    if st == n:
        print(0)
        break
    st += 1
