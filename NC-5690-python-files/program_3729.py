def verifSuiteAriGeo(liste,a,b):
  res=False
  c=liste
  for i in range(len(liste)-1):
    d=a*liste[i]+b
    c.append(d)
  return c