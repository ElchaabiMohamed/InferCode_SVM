def verifSuiteAriGeo(liste,a,b):
    if len(liste)==0:
      res=True
    else:
      res=True
      for i in range(1,len(liste)):
        if liste[i]==a*liste[i-1]+b:
          res=True
        else:
          res=False
    return res