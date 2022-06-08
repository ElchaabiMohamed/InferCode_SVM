def compteChiffre(chiffre,nombre):
  cpt=0
  trouve=False
  i=0
  while i<len(nombre) and not trouve:
    if chiffre in nombre:
      cpt+=1
    i+=1
  return cpt