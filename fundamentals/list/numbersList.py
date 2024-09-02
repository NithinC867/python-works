numbers=[12,14,15,17,19,11,10,22,21]
length=len(numbers)

for i in range(0,len(numbers)):
    if numbers[i]%2==0:
        print(numbers[i])


total=0
for i in range(0,len(numbers)):
    total+=numbers[i]
print(total)

odd_sum=0
for i in range(0,len(numbers)):
    if numbers[i]%2!=0:
        odd_sum+=numbers[i]
print(odd_sum)