def verifSuiteAriGeo(liste,a,b):
  res=False
  c=[]
  e=[]
  for i in range(len(liste)-1):
    d=a*liste[i]+b
    c.append(d)
    e.extend(c)
  return c