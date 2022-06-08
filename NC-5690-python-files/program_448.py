def nbChiffres(nombre):
  i=0
  while nombre!=0:
    nombre=nombre//10    
  i+=1
  if nombre==0:
    i=1
  return i