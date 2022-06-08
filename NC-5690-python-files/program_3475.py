def compteChiffre(chiffre,nombre):
  res=0
  nombre=str(nombre)
  chiffre=str(chiffre)
  for elem in nombre:
    if elem == chiffre:
      res=res+1
  return res