def suiteGeo(liste):
    if len(liste)==0 or len(liste)==1:
      res=True
    else:
      res=True
      for i in range(1,len(liste)):
        if liste[i-1]==0:
          res=False
        else:
          x=liste[1]/liste[0]
          if liste[i+1]!=x*liste[i]:
            res=False
    return res