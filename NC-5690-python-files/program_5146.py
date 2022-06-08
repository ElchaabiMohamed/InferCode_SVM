def verifSuiteAriGeo(liste,a,b):
  if liste==[]:
    res=True
  c=[liste[0]]
  res=False
  for i in range(len(liste)-1):
    d=a*liste[i]+b
    c.append(d)
  return c