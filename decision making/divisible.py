# num=int(input("enter the number "))

# if num%15==0:
#     print("fizzbuzz")

# elif num%5==0:
#     print("buzz")

# elif num%3==0:
#     print("fizz")

# else:
#     print("invalid")


#2nd

num=int(input("enter the number"))

result=""

if num%3==0:
    result=result+"buzz"

if num%5==0:
    result=result+"fuzz"

print(result)