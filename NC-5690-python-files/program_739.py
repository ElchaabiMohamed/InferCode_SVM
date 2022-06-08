def compteChiffre(chiffre,nombre):
  liste=[]
  chif=0
  res=0
  i=0
  if nombre==0 :
    res.append(nombre)
  else :
    while nombre!=0 :
      chiffre=nombre%10
      liste.append(chif)
      nombre=nombre//10
  
  while i<len(liste) :
    if liste[i]==chiffre :
      res+=1
    i+=1
  return res