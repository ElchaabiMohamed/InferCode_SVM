def maximum(liste):
    res=0
    for elem in liste:
        if elem>res:
        	res=elem
    res=liste[0]
    for elem in liste:
      	if elem>res:
        	res>elem
    return res