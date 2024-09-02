from re import fullmatch

f=open("C:\\Users\\HP\\Desktop\\PythonJuneWorks\\re_expression\\domail.txt")
pattern="[\\w\\W]+\\.com"
for line in f:
    domain=line.rstrip("\n")
    matcher=fullmatch(pattern,domain)
    if matcher !=None:
        print(domain)