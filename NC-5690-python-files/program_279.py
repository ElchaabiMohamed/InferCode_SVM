def verifSuiteAriGeo(liste,a,b):
  res=False
  c=[]
  for i in range(len(liste)):
    c=a*liste[i]+b
    c+=liste[-1]
  return c