def compteChiffre(chiffre,nombre):
  ok=True
  cpt=0
  i=0
  while i<len(nombre) and ok:
    if chiffre==nombre[i]:
      cpt=cpt+1
    i=i+1
  return cpt