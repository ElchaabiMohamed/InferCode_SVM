def compteChiffre(chiffre,nombre):
  nbr=str(nombre)
  chffre=str(chiffre)
  i=0
  res=0
  while i<len(nbr):
    if chffre==nbr[i]:
      res+=1
    i+=1
  return res