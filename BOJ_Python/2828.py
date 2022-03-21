N, M = map(int,input().split())
J = int(input())

basket = [1] # 가장 처음에 바구니는 왼쪽 M간을 차지하고 있다.
if M != 1:
    basket.append(M)
result = 0
for _ in range(J):
    W = int(input())
    if basket[0] <=  W <= basket[-1]:
        continue
    elif W > basket[-1]:
        gap = W - basket[-1]
        basket = list(map(lambda x: x + gap, basket))
        result += gap
    elif W < basket[0]:
        gap = basket[0] - W
        basket = list(map(lambda x: x - gap, basket))
        result += gap
    
print(result)
