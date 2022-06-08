def compteChiffre(chiffre,nombre):
  if chiffre==0 or nombre==0:
    res=1
  res=0
  while nombre!=0:
    nombre=nombre//10
    if nombre%10==chiffre:
      res+=1
  return res