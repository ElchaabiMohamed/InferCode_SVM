def verifSuiteAriGeo(liste,a,b):
  res=False
  c=[]
  for i in range(len(liste)-1):
    d=a*liste[i]+b
    d[0]+c.append(d)
  return c