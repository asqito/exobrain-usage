with open('./result.txt', 'r', encoding='utf-8') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
    originstr: str = file.read()

str1 = '"word":'
str2 = '"dependency"'

str1idxlist = []
str2idxlist = []

str1idx = originstr.find(str1)
str1idxlist.append(str1idx)

str2idx = originstr.find(str2)
str2idxlist.append(str2idx)

# 원본 스트링에서 파싱할 위치 찾기 - "word": 인덱스 찾아서 저장
while originstr[str1idx + 1:].find(str1) != -1:
    str1idx = originstr[str1idx + 1:].find(str1) + str1idx + 1
    str1idxlist.append(str1idx)

# 원본 스트링에서 파싱할 위치 찾기 - "dependency" 인덱스 찾아서 저장
while originstr[str2idx + 1:].find(str2) != -1:
    str2idx = originstr[str2idx + 1:].find(str2) + str2idx + 1
    str2idxlist.append(str2idx)

# print(str1idxlist)
# print(str2idxlist)

# "word":에서 "dependency" 까지 읽어서 파일에 쓰기
i = 0
f = open("./result_sum.txt",'w')

str1idxlist_cnt= len(str1idxlist)
# print("길이 : ", str1idxlist_cnt)

while i < str1idxlist_cnt:
    strtmp = originstr[str1idxlist[i]:str2idxlist[i]]

    f.write(strtmp)
    i = i + 1

f.close()
