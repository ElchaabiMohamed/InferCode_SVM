def verifSuiteAriGeo(liste,a,b):
  calc=0
  i=0
  lres=[]
  while i<len(liste):
    calc=a*calc+b
    lres.append(calc)
    i+=1
  return lres