def verifSuiteAriGeo(liste,a,b):
  calc=0
  i=0
  lres=[]
  ok=None
  while i<len(liste):
    calc=a*calc+b
    lres.append(calc)
    i+=1
  if lres in liste:
    ok=True
  else:
    ok=False
  return ok