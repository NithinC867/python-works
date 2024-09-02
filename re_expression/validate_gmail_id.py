from re import fullmatch

gmail_id=input("enter your gmail id")
pattern="\\w[\\w\\._]*@gmail.com"
finder=fullmatch(pattern,gmail_id)
print("invalid" if finder==None else "valid")