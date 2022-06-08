def verifSuiteAriGeo(liste,a,b):
  res=False
  c=[]
  for i in range(len(liste)-1):
    d=a*liste[i]+b
    c.append(d)
  for i in range(0,len(liste),0):
    c=liste[i]+c
  return c