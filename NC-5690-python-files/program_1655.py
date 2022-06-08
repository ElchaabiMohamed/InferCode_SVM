def quatrePlus100(liste):
    res=[]
    i=0
    nb=0
    for i in range(len(liste)):
      if liste[i]>100 and nb<4:
        res=res+[liste[i]]
        nb=nb+1
      i=i+1
    return res