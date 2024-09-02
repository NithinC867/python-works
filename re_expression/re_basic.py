from re import finditer

text="hello world hello world hello world hello"

finder=finditer("world",text)
count=0
for f in finder:
    print(f.start(),"==",f.group())
    count+=1
print("no.of world",count)