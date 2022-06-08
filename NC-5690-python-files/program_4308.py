def verifSuiteAriGeo(liste,a,b):
  res=False
  c=[]
  for i in range(len(liste)):
    d=a*liste[i]+b
    c.append(d)
  return c