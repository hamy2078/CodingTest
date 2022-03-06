import sys

N = int(sys.stdin.readline())

num_list = []
for _ in range(N):
    num = sys.stdin.readline()
    num_list.append(int(num))

num_list.sort()
for i in range(N):
    num = num_list[i]
    sys.stdout.write(str(num)+'\n')
