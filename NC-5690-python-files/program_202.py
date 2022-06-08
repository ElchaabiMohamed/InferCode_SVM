def quatrePlus100(liste):
  res = []
  cpt = 0
  i = 0
  while cpt < 4 and i < len(liste):
    if liste[i] > 100 :
      res.append(liste[i])
      cpt = cpt + 1
    i = i + 1
  return res 
