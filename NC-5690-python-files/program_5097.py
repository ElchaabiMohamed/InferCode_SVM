def compteChiffre(chiffre,nombre):
  res=0
  while nombre!=0:
    nombre=nombre//10
    if nombre[i]==chiffre:
      res+=1
  return res