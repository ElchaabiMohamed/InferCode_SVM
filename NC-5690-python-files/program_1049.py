def verifSuiteAriGeo(liste,a,b):
    if len(liste)==0:
      res=True
    else:
      res=False
      i=1
      while i<len(liste) and res:
        if liste[i]==a*liste[i-1]+b:
          res=True
      return res
    