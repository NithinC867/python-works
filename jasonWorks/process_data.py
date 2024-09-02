from json import load

f=open("C:\\Users\\HP\\Desktop\\PythonJuneWorks\\jasonWorks\\data.json")

movies=load(f)

for m in movies:
    print(m.get("title"))

