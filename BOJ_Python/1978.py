n = int(input())

cnt = 0
number = map(int,input().split())
for num in (number):
    flag = 1
    if num <= 1:
        flag = 0
    else:
        for i in range(2,num):
            if num % i == 0:
                flag = 0
                break
    if flag == 1:
        cnt+=1
print(cnt)
