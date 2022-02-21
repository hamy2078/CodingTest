import math
a, b, v = map(int, input().split())

# last day
day = 1
v -= a

day += math.ceil(v/(a-b))

print(day)
