def compteChiffre(chiffre,nombre):
  res=0
  res.append(nombre%10)
  for i in range(len(nombre)):
    if nombre[i]==chiffre:
      res+=1
  return res