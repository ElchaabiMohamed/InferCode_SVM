def compteChiffre(chiffre,nombre):
  res=0
  for elem in nombre:
    nombre=nombre//10
    if nombre[i]==chiffre:
      res+=1
  return res