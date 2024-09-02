mobiles=[

    {"id":100,"title":"s23 ultra","brand":"samsung","price":12500,"network":"5g"},
    {"id":101,"title":"s23","brand":"samsung","price":54000,"network":"4g"},
    {"id":102,"title":"edge14pro","brand":"moto","price":25000,"network":"5g"},
    {"id":103,"title":"edgeneo","brand":"moto","price":22000,"network":"4g"},
    {"id":104,"title":"redminote13pro","brand":"mi","price":25000,"network":"5g"},
    {"id":105,"title":"redmi13","brand":"mi","price":12000,"network":"4g"},
]
mobile_name=[nm.get("title") for nm in mobiles]
# print(mobile_name)

brand_name=[bnd.get("brand") for bnd in mobiles]
# print(set(brand_name))


samsung=[sam.get("title") for sam in mobiles if sam.get("brand")=="samsung"]
# print(samsung)

midrange=[mid.get("title") for mid in mobiles if mid.get("price")>23000 and mid.get("price")<40000]
# print(midrange)



def costly(mob):
    return mob.get("price")
costly_mobile=max(mobiles,key=costly)
print(costly_mobile)

cheapest_mobile=min(mobiles,key=costly)
print(cheapest_mobile)

sorted_mobile=sorted(mobiles,key=costly,reverse=True)
print()
