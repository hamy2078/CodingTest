n = int(input())
for _ in range(n):
    string = input()
    stack = []
    flag = 1
    for i in string:
        if i == '(':
            stack.append(i)
        else: # if i == ')':
            try:
                del stack[0]
            except:
                flag = 0
                break
    # 정상적으로 반복문 종료시
    if len(stack) == 0 and flag == 1:
        print('YES')
    else:
        print('NO')
