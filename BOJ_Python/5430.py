t = int(input())

for _ in range(t):
    order = list(input())
    N = int(input())
    number = input()
    if N == 0:
        number = []
    elif N == 1:
        number = [number[1]]
    else:
        number = number[1:-1].split(',')
        
    # print(order,number)
    re = False # 뒤집기 여부 
    front, back = 0,0 # 앞뒤로 삭제할 원소의 개수
    for i in order:
        if i == "R":
            re = not re
        else:
            if re == False:
                front += 1
            else:
                back += 1
    if front + back <= N:
        number = number[front:N-back]
        if re == True:
            number.reverse()
        print('['+','.join(number)+']')
    else: # 삭제할 개수가 숫자보다 많음
        print("error")
