
numbers = [10, 10, 20, 20, 20, 21, 22, 23]
count={}
for num in numbers:
    if num in count:
        count[num]+=1
    else:
        count[num]=1
print(count)
non_repeating=[num for num,counts in count.items() if counts==1]
print(f"non repeating numbers are{non_repeating}")
