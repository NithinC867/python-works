f_read=open("C:\\Users\\HP\\Desktop\\PythonJuneWorks\\filework\\years.txt")
century=open("C:\\Users\\HP\\Desktop\\PythonJuneWorks\\filework\\century.txt","w")
non_century=open("C:\\Users\\HP\\Desktop\\PythonJuneWorks\\filework\\non_century.txt","w")

for year in f_read:
    y=int(year.rstrip("\n"))
    if y%100==0:
        century.write(str(y)+"\n")
    else:
        non_century.write(str(y)+"\n")