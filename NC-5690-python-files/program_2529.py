def quatrePlus100(liste):
    res=0
    i=0
    while i!=4 :
      if len(liste)>100 :
        res=res+liste[i]
        i=i+1
    return res