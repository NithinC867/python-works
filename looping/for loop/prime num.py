num=int(input("enter number"))
isPrime=True

for i in range(2,num):
    if num%i==0:
        isPrime=False
        break
print(f"{num} is a prime num" if isPrime==True else "not a prime" )