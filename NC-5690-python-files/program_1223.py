def verifSuiteAriGeo(liste,a,b):
    if len(liste)==0:
      res=True
    else:
      res=True
      i=0
      while i<len(liste) and res:
        if liste[i+1]!=a*liste[i]+b:
          res=False
      return res
    