def verifSuiteAriGeo(liste,a,b):
  res=False
  c=[]
  for i in range(len(liste)-1):
    d=a*liste[i]+b
    c.append(d)
    d=liste[0]+d
  return c