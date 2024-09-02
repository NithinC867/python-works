num=[0,2,6,8]
missing_num=0

for i in num:
    if i==missing_num and i%2==0:
        missing_num+=2
print(missing_num)