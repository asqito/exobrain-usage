# 키워드 리스트 불러오기
with open('./wordlist.txt', 'r') as file:
    wordlistorg: str = file.read()

# print(wordlistorg)

# 태그 리스트 불러오기
with open('./taglist.txt', 'r', encoding='utf-8') as file:
    taglist: str = file.read()

# print("taglist:", taglist)


temp1 = []
temp2 = []
temp3 = []

temp1 = wordlistorg.split() # 단어 단위로 잘라서 넣기
# print('temp1:', temp1)

temp2 = taglist.split()
# print('temp2:', temp2)

f3 = open("./wordlisttag.txt", 'w')

for i in temp1:
    if i in temp2:
        temp3.append(i)
        temp3.append('\n')

# print(temp3)

f3.writelines(temp3)
f3.close()