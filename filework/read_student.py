f=open("C:\\Users\\HP\\Desktop\\PythonJuneWorks\\filework\\students.txt","r")
students=[]
for stud in f:
    students.append(stud.rstrip("\n"))
print(students)