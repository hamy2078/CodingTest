while True:
    number = input()
    if number == '0': break
    while True:
        first = number[0]
        end = number[-1]
        number = number[1:-1]
        if first != end:
            print("no")
            break
        if len(number) == 0:
            print("yes")
            break
