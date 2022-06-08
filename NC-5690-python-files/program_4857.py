def sommeNbPairs(liste):
  somme=0
  if liste==[]:
    somme=0
  for elem in liste:
    if elem%2==0:
      somme=somme+elem
  return somme