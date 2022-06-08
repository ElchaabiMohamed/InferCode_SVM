def compteChiffre(chiffre,nombre):
  cpt=0
  chiffre=int(chiffre)
  nombre=int(nombre)
  for i in range(nombre):
    if nombre[i]==chiffre:
      cpt=cpt+1
    i=i+1
  return cpt