def verifSuiteAriGeo(liste,a,b):
  if liste==[]:
    res=True
  c=[]
  res=False
  for i in range(len(liste)-1):
    d=a*liste[i]+b
    c.append(d)
  for i in range(0,len(liste),0):
    c=[liste[0]]+c
  return c