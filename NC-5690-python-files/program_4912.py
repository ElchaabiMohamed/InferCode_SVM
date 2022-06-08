def nbChiffres(nombre):
  res=0
  while nombre!=0:
      nombre=nombre//10
      res+=1
  if res==0:
    res=1
  return res