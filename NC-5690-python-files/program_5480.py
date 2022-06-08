def nbChiffres(nombre):
  res =0
  while nombre//10!=nombre:
    nombre//=10
    res+=1
  return res+1