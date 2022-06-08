def minimum(liste):
    res=liste[0]
    for i in liste:
      if liste[i]<res:
        res=liste[i]
    return res