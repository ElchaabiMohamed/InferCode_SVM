def compteChiffre(chiffre,nombre):
  res=0
  for i in range(nombre):
    if i==chiffre:
      res=res+1
  return res