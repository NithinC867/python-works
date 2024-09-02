text="abcddefabcd"

word_count={}

for c in text:
    if c in word_count:
        print(c,"is the first recursive charector")
        break

    else:
        word_count[c]=1