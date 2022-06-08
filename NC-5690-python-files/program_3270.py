def compteChiffre(x,y):
  cpt=0
  i=0
  for i in range(x):
    if x[i]==y:
      cpt=cpt+1
    i=i+1
  return cpt