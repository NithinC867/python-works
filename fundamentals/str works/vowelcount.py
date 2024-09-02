text="pneumonoultramicroscopicsilicovolcanoconiosis"
vowels="aeiou"

vcount=0

for ch in text:
    if vowels.count(ch)!=0:
        vcount+=1
print(vcount)