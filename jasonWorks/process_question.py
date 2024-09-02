from json import load

f=open("C:\\Users\\HP\\Desktop\\PythonJuneWorks\\jasonWorks\\question.json",encoding="UTF-8")

data=load(f)

# name_of_thr_contries=[c.get("name") for c in data]
# print(name_of_thr_contries)

# indipentent_contry=[i.get("name") for i in data if i.get("independent")==True]
# print(indipentent_contry)

# sothern_europe_countrys=[s.get("name") for s in data if s.get("subregion")=="Southern Europe"]
# print(sothern_europe_countrys)

# area_under_100000=[a.get("name") for a in data if a.get("area")<=100000]
# print(area_under_100000)

# flags=[f.get("flag") for f in data ]
# print(flags)

# asian_contries=[c.get("name") for c in data if c.get("region")=="Asia"]
# print(asian_contries)


region_summery={}
for c in data:
    region_name=c.get("region")
    if region_name in region_summery:
        region_summery[region_name]+=c.get("area",0)
    else:
        region_summery[region_name]=c.get("area",0)
# print(region_summery)

value_key=[(v,k) for k,v in region_summery.items()]

print(max(value_key))