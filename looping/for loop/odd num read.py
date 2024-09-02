limit=int(input("enter the limit"))
start=int(input("enter the start"))

for i in range(start,limit):
    if i%2!=0:
        print(i)