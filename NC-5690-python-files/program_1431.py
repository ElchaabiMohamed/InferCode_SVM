def doubleChiffre(nombre):
  res=True
  cpt=nombre
  ctp2=0
  while res==True:
    cpt2=cpt%10
    cpt=cpt//10
    if cpt==cpt2:
      res=False
  return res

    