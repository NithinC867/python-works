expenses=[12000,10000,16000,11000,20000,13000,8000,7500,17000,13000]

exp_count=len(expenses)

# for i in range(0,exp_count):
    # if expenses[i]>15000:

    #     print(expenses[i])
    
total_exp=0

for i in range(0,len(expenses)):
    total_exp=total_exp+expenses[i]
print(total_exp)


#avg

avg=total_exp/len(expenses)
print(avg)