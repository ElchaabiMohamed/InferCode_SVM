def verifSuiteAriGeo(liste,a,b):
  res=True
  i=1
  while i<len(liste):
    if liste[i]!=a*liste[i-1]+b:
      res=False
    i+=1
  return res
def suiteAriGeo(liste):
  i=1
  res=True
  if len(liste)>3:
    ecart1=liste[1]-liste[0]
    ecart2=liste[2]-liste[1]
    a=ecart2/ecart1
    b=liste[1]-a*liste[0]
    while i<len(liste):
      if verifSuiteAriGeo(liste,a,b)!=True:
        res=False
      i+=1 
  return res