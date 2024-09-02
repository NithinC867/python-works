num=int(input("enter the number"))
og=num
result=0

while(num!=0):
    digit=num%10
    result=result*10+digit
    num=num//10
print("palindrome" if result==og else "not a palindrome")
