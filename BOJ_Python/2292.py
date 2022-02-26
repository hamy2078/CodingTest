n = int(input())

room = 1
i = 0
while True:
    room +=  6*(i)
    i+=1
    if n <= room:
        print(i)
        break
