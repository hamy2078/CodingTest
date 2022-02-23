k = int(input())

num = []
for i in range(k):
    number = int(input())
    if number == 0:
        del num[-1]
    else:
        num.append(number)

print(sum(num))
