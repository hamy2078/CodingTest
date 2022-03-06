import sys

N = int(sys.stdin.readline())

acc_sum = [] * N

for i in range(N):
    num = list(map(int,sys.stdin.readline().split()))
    line = []
    for j in range(len(num)):
        if i == 0:
            line.append(num[0])
        else:
            if j == 0:
                line.append(acc_sum[i-1][j] + num[j])
            elif j == len(num)-1:
                line.append(acc_sum[i-1][j-1] + num[j])
            else:
                line.append(max(acc_sum[i-1][j-1],acc_sum[i-1][j])+num[j])
    acc_sum.append(line)

sys.stdout.write(str(max(acc_sum[N-1])))
