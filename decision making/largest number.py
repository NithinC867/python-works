num1=int(input("enter the first number" ))
num2=int(input("enter the second number" ))
num3=int(input("enter the third number" ))

if num1>num2 and num1>num3 :
    print(f"{num1} is the largest number")

elif num1<num2 and num2>num3 :
    print(f"{num2} is the largest number")

else:
    print(f"{num3} is the largest number")
