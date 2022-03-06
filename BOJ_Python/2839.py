N = int(input())

bags = [5001] * (5001)

bags[3] = bags[5] = 1

for i in range(6, N+1):
    bags[i] = min(bags[i-3], bags[i-5])+1

if bags[N] >= 5001:
    bags[N] = -1
print(bags[N])
