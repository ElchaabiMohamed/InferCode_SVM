def verifSuiteAriGeo(liste,a,b):
  suite=liste[0]
  i=1
  res=True
  while i<len(liste) and res==True:
    suite=a*suite+b
    if suite==liste[i]:
      res=True
    else:
      res=False
    i+=1
  return res
    
    
    