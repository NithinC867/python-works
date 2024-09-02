num=[3,5,6,11,5,9,5,7,8]

largest_number=num[0]
second_largest=num[0]


for i in num:
    if i>second_largest and i>largest_number:

        second_largest=largest_number

        largest_number=i
print(f"second largest number is {second_largest}")

    # elif i>second_largest and i>largest_number:
    #     second_largest=i
    #     print(f"second largest number is {second_largest}")