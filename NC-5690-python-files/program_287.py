def verifSuiteAriGeo(liste,a,b):
  res=False
  c=[]
  for i in range(-1,len(liste)-1):
    d=a*liste[i]+b
    c.append(d)
  return c