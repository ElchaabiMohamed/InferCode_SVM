def suiteGeo(liste):
  res = True
  i = 0
  if liste == [] or len(liste) == 1 :
    res = True
  else :
    if liste [0] == 0 and liste [1] != 0:
      res = False
    else :
      raison = liste[1]/liste[0]
  while res and i < len(liste)-1 :
    if liste[i]*raison != liste[i+1]:
      res = False
    i = i + 1
  return res
