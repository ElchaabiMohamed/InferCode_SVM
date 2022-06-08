def compteChiffre(chiffre,nombre):
  res=0
  for i in range(len(nombre)):
    res.append(nombre%10)
    if nombre[i]==chiffre:
      res+=1
  return res