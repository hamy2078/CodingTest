n = int(input())
A = list(map(int, input().split()))
m = int(input())
X = list(map(int, input().split()))

# X가 A에 있는 숫자인지 검색하는 것보다
# 교집합 속에 있는 숫자인가 검색하는 게 속도면에서 좋다.

intersection = set(X).intersection(set(A))

for i in X:
    if i in intersection:
        print(1)
    else:
        print(0)
