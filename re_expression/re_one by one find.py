from re import finditer

# text="abc123bc@$%"
# pattern="[abc]"
# find=finditer(pattern,text)

# for m in find:
#     print(m.start(),"==",m.group())


# text1="abcdef123bc@$%"
# pattern="[a-d]"
# find1=finditer(pattern,text1)

# for f in find1:
#     print(f.start(),"==",f.group())


text1="abcbgihs13ve3fg@$%"
# # pattern="[c-h]|t-z]"
# # pattern="\d"
# pattern="\\D"

# find1=finditer(pattern,text1)

# for f in find1:
#     print(f.start(),"==",f.group())



pattern="\\w"
matcher=finditer(pattern,text1)
for i in matcher:
    print(i.start(),"==",i.group())