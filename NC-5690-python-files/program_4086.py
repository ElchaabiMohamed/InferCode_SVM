def maximum(liste):
    res=0
    for elem in liste:
        if elem>res:
        	res=elem
    for elem in liste:
        if elem<0:
            res=elem
    return res