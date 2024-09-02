from json import load

f=open("C:\\Users\\HP\\Desktop\\PythonJuneWorks\\jasonWorks\\products.json",encoding="UTF-8")

items=load(f)
# print(len(items))


# for p in items:
#     print(p.get("title"))

# product_titles=[p.get("title") for p in items]
# print(product_titles)

# jwellery_category=[j.get("title") for j in items if j.get("category")=="jewelery"]
# print(jwellery_category)


# product_greater=[g.get("title") for g in items if g.get("price")>100]
# print(product_greater)

product_available=[g.get("title") for g in items if g.get("price")>=100 and g.get("price")<=150]
print(product_available)

