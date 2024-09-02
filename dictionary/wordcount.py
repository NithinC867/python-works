text="hai hello hello hai hai hello"

word=text.split(" ")

wordcount={}

for w in word:
    if w in wordcount:
        wordcount[w]+=1
    else:
        wordcount[w]=1
print(wordcount)