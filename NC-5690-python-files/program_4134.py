def compteChiffre(x,y):
  cpt=0
  i=0
  for i in range(y):
    if y[i]==x:
      cpt=cpt+1
    i=i+1
  return cpt