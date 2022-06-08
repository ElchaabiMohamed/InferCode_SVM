def maximum(liste):
    res=liste[0]
    for i in range (liste):
      if liste[i]>res :
        res=liste[i]
    return res