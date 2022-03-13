from itertools import combinations
import sys

while True:
    lotto = list(map(int,sys.stdin.readline().split()))
    if lotto[0] == 0: break
    else:
        combi = list(combinations(lotto[1:],6))
        for i in combi:
            for j in i:
                sys.stdout.write(str(j)+' ')
            sys.stdout.write('\n')
    sys.stdout.write('\n')
