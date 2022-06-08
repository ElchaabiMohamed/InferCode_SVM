def verifSuiteAriGeo(liste,a,b):
  if liste==[]:
    res=True
  c=[]
  res=False
  for i in range(len(liste)-1):
    d=a*liste[i]+b
    c.append(d)
    c=[liste[0]]/len(liste)+c
  return c