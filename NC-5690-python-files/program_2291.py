def nbChiffres(nombre):
  cpt=1
  while nombre!=0:
    if nombre//10!=0:      
      cpt=cpt+1
    nombre=nombre//10
  return cpt
   