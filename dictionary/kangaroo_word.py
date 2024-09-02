source_word="CHICKEN"
target_word="HEN"

wordcount={}
for c in source_word:
    if c in wordcount:
        wordcount[c]+=1
    else:
        wordcount[c]=1

kangaroo_word=True

for c in target_word:
    if c in wordcount and wordcount.get(c)>0:
        wordcount[c]-=1
    else:
        kangaroo_word=False
print(kangaroo_word) 