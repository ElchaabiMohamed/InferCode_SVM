def nbChiffres(nombre):
  res=nombre
  cpt=0
  while res>0:
    res=res//10
    cpt=cpt+1
  res=cpt
  if res==0:
    res=1
  return res