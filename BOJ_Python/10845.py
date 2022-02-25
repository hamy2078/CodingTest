# queue
'''
input() 보다 sys.stdin.readline()을 사용하면 더 빠르게 입력이 가능하다.
마찬가지로 print()보다 sys.stdout.write()가 속도가 빠르다.
'''

import sys

n = int(sys.stdin.readline())
queue = []
cnt = 0 
for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        queue.append(command[1])
        cnt += 1
    elif command[0] == 'pop':
        if cnt == 0:
            sys.stdout.write(str(-1)+'\n')
        else:
            sys.stdout.write(queue.pop(0)+'\n')
            cnt -= 1
    elif command[0] == 'front':
        if cnt == 0:
            sys.stdout.write(str(-1)+'\n')
        else:
            sys.stdout.write(queue[0]+'\n')
    elif command[0] == 'back':
        if cnt == 0:
            sys.stdout.write(str(-1)+'\n')
        else:
            sys.stdout.write(queue[-1]+'\n')
    elif command[0] == 'size':
        print(cnt)
    elif command[0] == 'empty':
        if cnt == 0:
            sys.stdout.write(str(1)+'\n')
        else:
            sys.stdout.write(str(0)+'\n')
