def compteChiffre(chiffre,nombre):
  cpt=0
  if nombre==0:
    cpt=cpt+1
  while nombre!=0:
    val=nombre%10
    nombre=nombre//10
    if val==chiffre:
      cpt=cpt+1
  
  return cpt