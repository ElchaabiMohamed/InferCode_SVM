def quatrePlus100(liste):
    res=[]
    i=0
    while i<len(liste):
      if liste[i]>100:
        res.append(liste[i])
      i=i+1
    return res