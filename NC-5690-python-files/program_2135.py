def suiteGeo(liste):
  i = 0
  j = 0
  raison = 0
  if liste == [] or len(liste) == 1 :
    res = True
  else :
    res = True 
  while raison == 0 and j < len(liste) - 1 :
    if liste[j] != 0 :
       raison = liste[j+1]/liste[j]
    j = j + 1
  while res and i < len(liste) - 1 :
    if liste[i]*raison != liste[i+1]:
      res = False
    i = i + 1
  return res
