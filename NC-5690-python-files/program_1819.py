def nbChiffres(nombre):
  cpt=0
  if nombre==0:
    cpt=1
  else:
    while nombre>=1:
      nombre=nombre//10
      cpt=cpt+1
  return cpt