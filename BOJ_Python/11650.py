n = int(input())

coordinates = []
for _ in range(n):
    x, y = map(int, input().split())
    coordinates.append([x,y])

coordinates.sort(key = lambda x: (x[0], x[1])) # 다중 조건 정렬
for x,y in coordinates:
    print(x,y)
