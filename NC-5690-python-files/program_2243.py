def verifSuiteAriGeo(liste,a,b):
  if liste==[]:
    res=True
  else:
    c=[]
    res=False
    for i in range(len(liste)-1):
      d=a*liste[i]+b
      c.append(d)
      c=liste[0]+c
      if c==liste:
        res=True
    return res