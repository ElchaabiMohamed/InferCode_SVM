def quatrePlus100(liste):
  if len(liste)==0:
    res=[]
  else:
    res=[]
    for i in range(len(liste)):
      if liste[i]>100:
        res=res+liste[i]
    return res