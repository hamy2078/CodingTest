n, k = map(int, input().split()) #n개의 동전 종류, k 가치의 합

coin = []
for _ in range(n):
    coin.insert(0,int(input()))

cnt = 0
for val in coin:
    if k // val != 0:
        cnt += k // val
        k = k % val
    if k == 0:
        break
print(cnt)
