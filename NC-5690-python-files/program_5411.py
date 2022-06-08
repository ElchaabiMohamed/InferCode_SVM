def stockerChiffres(nombre):
  res=[]
  chiffre=0
  if nombre==0 :
    res.append(nombre)
  else :
    while nombre!=0 :
      chiffre=nombre%10
      res.append(chiffre)
      nombre=nombre//10
  
  return res