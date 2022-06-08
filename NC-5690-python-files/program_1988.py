def quatrePlus100(liste):
    res=[]
    i=0
    nb=0
    while i<=len(liste) or nb<4:
      if liste[i]>100:
        res=res+[liste[i]]
        nb=nb+1
      i=i+1
    return res