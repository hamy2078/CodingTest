n = int(input())

word_list = []
for i in range(n):
    word_list.append(input())


word_list = list(set(word_list))

word_list.sort() # 사전순으로
word_list.sort(key=len) # 길이 순으로 

for i in range(len(word_list)):
    print(word_list[i])
