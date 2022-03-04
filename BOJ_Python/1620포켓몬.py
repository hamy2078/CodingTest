import sys
n, m = map(int, sys.stdin.readline().split())

pokemon_name = {sys.stdin.readline().rstrip():i+1 for i in range(n)}
pokemon_num = dict(zip(pokemon_name.values(),pokemon_name.keys()))

for _ in range(m):
    com = sys.stdin.readline().rstrip()
    try:
        com = int(com)
        sys.stdout.write(pokemon_num[com]+'\n')
    except:
        sys.stdout.write(str(pokemon_name[com])+'\n')
