def verifSuiteAriGeo(liste,a,b):
    if len(liste)==0:
      res=True
    else:
      res=True
      for i in range(0,len(liste)):
        if liste[i+1]==a*liste[i]+b:
          res=True
        else:
          res=False
    return res
    