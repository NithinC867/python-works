heightin_cm=int(input("enter your height "))
weight=int(input("enter your weight" ))

height=heightin_cm/100

result=weight/height**2

print(result)

if result<=19 :
    print("under weight")

elif result>19 and result<=25 :
    print("Normal weight")

elif result>25 and result<=30 :
    print("Over weight")

else:
    print("obesity")