arr=[2345]
sum=0

for i in range(0,len(arr)):
    sum+=sum[i]
    if sum==6:
        print(sum[i])