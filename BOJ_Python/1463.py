# 메모이제이션 사용
import sys
n = int(sys.stdin.readline())

array = [1000000]*(n+3)

array[1] = 0
array[2] = array[3] =1

for i in range(4,n+1):
    if i % 3 == 0 and i % 2 == 0:
        array[i] = min([array[i//3], array[i//2], array[i-1]])+1
    elif i % 3 == 0:
        array[i] = min([array[i//3], array[i-1]])+1
    elif i % 2 == 0:
        array[i] = min([array[i//2], array[i-1]])+1
    else:
        array[i] = array[i-1]+1
        
print(array[n])
