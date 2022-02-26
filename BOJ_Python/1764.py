n, m = map(int, input().split())

Nlisten = set()
for _ in range(n):
    Nlisten.add(input())
Nlook = set()
for _ in range(m):
    Nlook.add(input())
result = Nlook.intersection(Nlisten)
result = sorted(result)
print(len(result))
for i in (result):
    print(i)
