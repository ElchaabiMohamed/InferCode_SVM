def compteChiffre(chiffre,nombre):
  ok=True
  cpt=0
  i=0
  while i<len(nombre) and ok:
    if nombre[i]==chiffre:
      cpt=cpt+1
    i=i+1
  return cpt