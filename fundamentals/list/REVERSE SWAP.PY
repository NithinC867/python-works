num=[10,11,12,13,14,15,16,17]

left=1

length=len(num)-1

if length%2!=0:
    right=length
else:
    right=length-1

while(left<right):
    (num[left],num[right])=(num[right],num[left])
    left=left+2
    right=right-2
print(num)