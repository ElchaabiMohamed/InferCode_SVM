def compteChiffre(chiffre,nombre):
  res=0
  for i in range (len(nombre)):
    if chiffre==nombre[i]:
      res=res+1
  return res
