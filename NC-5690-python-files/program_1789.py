def quatrePremierSuperieurACent(liste):
  i=0
  res=[0]*len(liste)
  while i<4:
    if liste[i]>100:
      res.append(liste[i])
    i=i+1
  return res