num=int(input("enter the number"))
previous=0
current=1
isfibi=False
next=previous+current

while(next<=num):
    next=previous+current
    if next==num:
        isfibi=True
        break
    previous=current
    current=next
print(isfibi)