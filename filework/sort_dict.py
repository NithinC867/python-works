placements={"testing":39,"python":45,"java":33,"c++":22}

def get_value(key):
    return placements.get(key)

srt=sorted(placements,key=get_value,reverse=True)
print(srt)