def suiteGeo(liste):
    if len(liste)==0:
      res=True
    else:
      res=True
      for i in range(1,len(liste)):
        x=liste[1]//liste[0]
        if liste[i]==0:
          res=False
        else:         
          if liste[i]==liste[i-1]*x:
            res=True
          else:
            res=False
    return res