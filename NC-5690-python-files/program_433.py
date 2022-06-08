def verifSuiteAriGeo(liste,a,b):
  res = True
  i = 0
  while res and i < len(liste)-1:
    if liste[i+1] != (a*liste[i]+b) :
      res = False
    i = i + 1
  return res

def suiteAriGeo(liste):
  if len(liste) < 3 :
    res = True
  else :
    ecart1 = liste[1]-liste[0]
    ecart2 = liste[2]-liste[1]
    if ecart1 == 0 or ecart2 == 0:
      a = 1
    else :
      a = ecart2/ecart1
    b = liste[1]-a*liste[0]
    res = verifSuiteAriGeo(liste,a,b)
  return res
