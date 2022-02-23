n = int(input())

member_list = []
for i in range(n):
    member_list.append(input().split())

member_list.sort(key = lambda x: int(x[0])) # 나이순으로

for i in range(n):
    age = member_list[i][0]
    name = member_list[i][1]
    print(age, name)
