num=[6,4,3,8,4,9,13,12]

smallest_num=num[0]

for i in num:
    if i<smallest_num:
        smallest_num=i

print(f"smallest number is {smallest_num}")