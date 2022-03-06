import sys

string = sys.stdin.readline().strip()
c = "a"
while True:
    sys.stdout.write(str(string.find(c))+' ')
    if c == "z":
        break
    c = chr(ord(c)+1)
