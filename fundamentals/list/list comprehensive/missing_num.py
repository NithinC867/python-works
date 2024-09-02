num=[0,1,2,3,5,6,7]
n=len(num)
sum_of_n=n*(n+1)/2
sum_of_current=sum(num)

missing_num=sum_of_n-sum_of_current

print(missing_num)
