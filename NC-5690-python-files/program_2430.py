def verifSuiteAriGeo(liste,a,b):
  res=True
  i=1
  while i<len(liste):
    if liste[i]!=a*liste[i-1]+b:
      res=False
    i+=1
  return res
def suiteGeo(liste):
  i=1
  a=1
  b=0
  while i<len(liste):
    if liste[i-1]==0:
      i+=1
    else:
      if liste[i]!=liste[i-1]:
        a=liste[i]/liste[i-1]
        b=liste[i]-a*liste[i-1]
    i+=1 
  return verifSuiteAriGeo(liste,a,b)