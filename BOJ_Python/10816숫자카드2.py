import sys
from collections import Counter
n = int(sys.stdin.readline())
cards = list(sys.stdin.readline().split())
cards = Counter(cards)

m = int(sys.stdin.readline())
nums = list(sys.stdin.readline().split())
for num in nums:
    try:
        print(cards[num],end=' ')
    except:
        print(0,end=' ')
