f=open("C:\\Users\\HP\\Desktop\\PythonJuneWorks\\filework\\news.txt")

wordlis=[]
for line in f:
    word=line.rstrip("\n").split(" ")

    for w in word:
        wordlis.append(w)
    print(wordlis)

wc={w:wordlis.count(w) for w in wordlis}
print(wc)


def get_value(key):
    return wc.get(key)
srt=sorted(wc,key=get_value,reverse=True)