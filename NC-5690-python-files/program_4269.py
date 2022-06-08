def doubleChiffre(nombre):
  res=False
  cpt=nombre
  ctp2=0
  while res==False:
    cpt2=cpt%10
    cpt=cpt//10
    if cpt==cpt2:
      res=True
  return res

    