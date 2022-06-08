def doubleChiffre(nombre):
  res=False
  cpt2=nombre%10
  cpt=nombre//10
  while not res and cpt!=0:
    if cpt2 == cpt%10 :
      res=True
    else :
      cpt2=cpt%10
      cpt=cpt//10
      
  return res