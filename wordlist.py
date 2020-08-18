# 키워드 리스트 만들기
with open('./result_sum.txt', 'r') as file:
    wordliststr: str = file.read()

wordidxstr1 = '"text":"'
wordidxstr2 = '","type":'

# 워드 위치 찾기
wordidx1 = wordliststr.find(wordidxstr1)
wordidx2 = wordliststr.find(wordidxstr2)

f1 = open("./wordlist.txt",'a')
# 위드 위치 찾아서 파일에 추가하기
while wordliststr[wordidx1 + 1:].find(wordidxstr1) != -1:
    wordidx1 = wordliststr[wordidx1 + 1:].find(wordidxstr1) + wordidx1 + 1
    wordidx2 = wordliststr[wordidx2 + 1:].find(wordidxstr2) + wordidx2 + 1

    wordtmp = wordliststr[wordidx1+8:wordidx2]
    # print(wordtmp)
    f1.write(wordtmp + '\n')


f1.close()



