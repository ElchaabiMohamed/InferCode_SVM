def compteChiffre(chiffre,nombre):
  ok=True
  i=0
  cpt=0
  while i<len(nombre) and okay:
    if chiffre==nombre[i]:
      cpt=cpt+1
    i=i+1
  return cpt