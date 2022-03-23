# 이미 가지고 있는 랜선의 개수 K, 그리고 필요한 랜선의 개수 N
K, N = map(int,input().split())

cable = []
for _ in range(K):
    cable.append(int(input()))

start, end = 1, max(cable)

while start <= end:
    mid = (start+end)//2
    count = 0 # 랜선의 개수
    for i in cable:
        count += i // mid

    if count < N:
        end = mid - 1
    else:
         start = mid + 1
print(end)
