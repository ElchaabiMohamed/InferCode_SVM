def verifSuiteAriGeo(liste,a,b):
  res=True
  i=1
  while i<len(liste):
    if liste[i]!=a*liste[i-1]+b:
      res=False
    i+=1
  return res
def suiteAri(liste):
  cpt=0
  i=1
  a=1
  b=0
  while i<len(liste) and cpt!=3:
    if liste[i]!=liste[i-1]:
      b=liste[i]-liste[i-1]
      cpt+=1
    i+=1 
  return verifSuiteAriGeo(liste,a,b)
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
def suiteAriGeo(liste):
  res=True
  if not suiteAri(liste) and not suiteGeo(liste):
    res=False
  return res