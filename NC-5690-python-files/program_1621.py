def maximum(liste):
    if len(liste)==0:
      res=None
    else:
      max=liste[0]
      for i in range(1,len(liste)):
        if liste[i]>max:
          res=liste[i]
    return res