vehicle_numbers=["KL50E6722","KL01A2366","KL23F3444"]

f=open("C:\\Users\\HP\\Desktop\\PythonJuneWorks\\filework\\vehicle_num.txt","w")
for num in vehicle_numbers:
    f.write(num+"\n")