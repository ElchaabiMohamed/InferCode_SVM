def compteChiffre(chiffre,nombre):
  res=0
  while nombre!=0:
    if nombre%10==chiffre:
      res=res+1
    nombre=nombre//10
  if nombre==0:
    res=1
  return res