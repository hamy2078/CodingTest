n = int(input())

end_num = 666
cnt = 1
while True:
    string = str(end_num)
    if '666' in string:
        if cnt == n:
            print(string)
            break
        cnt += 1
    end_num += 1
