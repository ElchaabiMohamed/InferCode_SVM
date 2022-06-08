def compteChiffre(chiffre,nombre):
  res=0
  cpt=0
  l=[]
  decomp=nombre
  if chiffre==0 and nombre==0:
    res=1
  while decomp!=0:
    l.append(decomp%10)
    decomp=decomp//10
    if l[cpt]==chiffre:
      res=res+1
    cpt=cpt+1
  return res