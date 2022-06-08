def sommeNbPairs(liste):
  res = 0
  for i in liste :
    if liste[i]%2 == 0 :
      res = res + liste[i]
  return res