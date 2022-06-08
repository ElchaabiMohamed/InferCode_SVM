def maximum(liste):
    if len(liste)==0:
        res=None
    else:
        res=liste[0]
    for elem in liste:
        if elem>res:
          res=elem
    return res