def compteChiffre(chiffre,nombre):
  res=0
  i=0
  if nombre==0:
    res=1
  while nombre!=0:
    if chiffre==nombre%10:
      res=res+1
    i=i+1
    nombre=nombre//10
  return res
