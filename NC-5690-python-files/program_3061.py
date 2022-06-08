def verifSuiteAriGeo(liste,a,b):
  if liste==[]:
    res=True
  c=[]
  f=[]
  res=False
  for i in range(len(liste)-1):
    d=a*liste[i]+b
    c.append(d)
    e=liste[0]
    f.append(e)
    f.extend(c)
  if f==liste:
    res=True
  return res