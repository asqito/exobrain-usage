with open('./wordlist.txt', 'r') as file:
    wordlistorg: str = file.read()

wordlist = wordlistorg.split()
wordCount = {}

for word in wordlist:
    wordCount[word] = wordCount.get(word, 0) + 1
    keys = sorted(wordCount.keys())


f2 = open("./wordlistCnt.txt", 'w')

for word in keys:
    # print(word + ':' + str(wordCount[word]))
    f2.write(word + ':' + str(wordCount[word]) + '\n')

f2.close()
