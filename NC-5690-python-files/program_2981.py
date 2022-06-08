def nbChiffres(nombre):
  cpt=0
  if nombre==0:
    cpt=1
  else:
    while nombre!=0:
      nombre=nombre//10
      cpt=cpt+1
  return cpt
