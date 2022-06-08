def ecart(liste):
    if len(liste)==0:
      res=None
    else:
      min=liste[0]
      for i in range(1,len(liste)):
        if liste[i]<min:
          min=liste[i]
      max=liste[0]
      for i in range(1,len(liste)):
        if liste[i]>max:
          max=liste[i]
    res=max-min
    return res