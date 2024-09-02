num=[1,3,2,5,9,7,4,13,17,11]
largest_num=num[0]

for i in num:
    if i > largest_num:
        largest_num=i
print(f"largest num = {largest_num}")