from itertools import combinations

n, m = map(int, input().split())

card = map(int, input().split())

combi = list(combinations(card,3))

Max = 0
for i in combi:
    total = sum(i)
    if total <= m and m - Max > m - total:
        Max = total
print(Max)
