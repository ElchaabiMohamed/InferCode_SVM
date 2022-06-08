def suiteGeo(liste):
  cpt=0
  i=1
  a=1
  b=0
  while i<len(liste) and cpt!=2:
    if liste[i-1]==0:
      i+=1
    else:
      if liste[i]!=liste[i-1]:
        a=liste[i]/liste[i-1]
        cpt+=1
    i+=1 
  return verifSuiteAriGeo(liste,a,b)