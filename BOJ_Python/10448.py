triangle = []
for n in range(1,50):
    triangle.append(int(n*(n+1)*0.5))
# print(triangle)
t = int(input())
for _ in range(t):
    num = int(input())
    flag = 0
    for i in triangle:
        if flag == 1: break
        for j in triangle:
            if flag == 1: break
            for k in triangle:
                if i + j + k == num:
                    print(1)
                    flag = 1
                    break
                    
    if flag == 0:
        print(0)
    
