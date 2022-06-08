def suiteAri(liste):
    if len(liste)==0:
      res=True
    else:
      res=True
      for i in range(1,len(liste)):
        x=liste[1]-liste[0]
        if liste[i]!=liste[i-1]+x:
          res=False
    return res