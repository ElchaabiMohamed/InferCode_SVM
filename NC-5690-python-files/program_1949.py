def compteChiffre(chiffre,nombre):
  res=0
  cpt=0
  l=[]
  decomp=nombre
  while decomp!=0:
    l.append(decomp%10)
    decomp=decomp//10
    if l[cpt]==chiffre:
      res=res+1
    cpt=cpt+1
  return res