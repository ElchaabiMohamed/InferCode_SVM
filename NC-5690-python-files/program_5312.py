def maximum(liste):
    if len(liste)==0:
      max=None
    else:
      max=liste[0]
      for i in range(1,len(liste)):
        if liste[i]>max:
          res=liste[i]
    