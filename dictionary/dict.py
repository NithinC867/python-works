mobile={"brand":"iqoo","name":"neo6","price":30000,"offer":500}

if "offer" in mobile:
    sell=mobile.get("price") - mobile.get("offer")
    print(sell)
else:
    print(mobile.get("price"))














# for k,v in mobile.items():
#     print(k,v)



    # get(key)
    # values()
    # keys()
