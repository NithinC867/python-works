num=int(input("enter the number"))

isprime=True

for i in range(2,num):
    if num%i==0:
        isprime=False
        break
print("is prime" if isprime==True else "not prime")