def compteChiffre(chiffre,nombre):
  res=0
  while nombre!=0:
    res.append(nombre%10)
    nombre=nombre//10
    if nombre==chiffre:
      res+=1
  return res