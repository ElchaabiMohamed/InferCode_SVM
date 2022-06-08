def nbChiffres(nombre):
  res =0
  if nombre==0:
    return 1
  while nombre//10!=nombre:
    nombre//=10
    res+=1
  return res