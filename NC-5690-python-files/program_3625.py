def verifSuiteAriGeo(liste,a,b):
  res = True
  i = 0
  while res and i < len(liste):
    if liste[i+1] != a*liste[i]+b :
      res = False
    i = i + 1
  return res