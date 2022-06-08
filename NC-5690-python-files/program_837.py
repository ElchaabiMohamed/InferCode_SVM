def verifSuiteAriGeo(liste,a,b):
  res=False
  c=[]
  for i in range(len(liste)):
    c=a*[liste[i]]+b
    if c==liste:
      res=True
  return res