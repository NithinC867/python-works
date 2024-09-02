f=open("C:\\Users\\HP\\Desktop\\PythonJuneWorks\\filework\\landslides.txt","r")

data=[]

for line in f:
    lst=line.rstrip("\n").split(" ")
    if len(lst) >= 3:
        dic={"state":lst[0],"year":lst[1],"death_count":int(lst[2])}
        data.append(dic)
print(data)


state_summery={}

for dic in data:
    state=dic.get("state")
    death_count=dic.get("death_count")
    if state in state_summery:
        state_summery[state]+=death_count
    else:
        state_summery[state]=death_count
    print(state_summery)