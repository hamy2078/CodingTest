import sys
T = int(sys.stdin.readline())

array = [[0,0]]*41

array[0] = [1,0]
array[1] = [0,1]
array[2] = [1,1]


for i in range(3,41):
    array[i] = [array[i-1][0]+array[i-2][0],array[i-1][1]+array[i-2][1]]

for _ in range(T):
    n = int(sys.stdin.readline())
    sys.stdout.write(str(array[n][0])+' '+str(array[n][1])+'\n')
