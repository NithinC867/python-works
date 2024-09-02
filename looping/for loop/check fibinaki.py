previous=0
current=1
num=int(input("enter the num"))

for i in range(1,11):
    next=previous+current
    if next==num:
        print("fibinaki")
    else:
        print("not")
    previous=current
    current=next