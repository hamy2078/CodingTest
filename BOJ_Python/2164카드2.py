import sys
n = int(sys.stdin.readline())

cards = [i+1 for i in range(n)]

while True:
    if len(cards) == 1:
        sys.stdout.write(str(cards[0]))
        break
    del cards[0::2] # 하나씩 제거하는 방법은 시간초과가 발생해 한번에 여러 숫자 제거
    
    if n % 2 == 1:
        cards.append(cards[0])
        del cards[0]
    n = len(cards)
