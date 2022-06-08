def compteChiffre(chiffre,nombre):
  liste=[]
  chif=0
  res=0
  i=0
  if nombre==0 :
    liste.append(nombre)
  else :
    while nombre!=0 :
      chif=nombre%10
      liste.append(chif)
      nombre=nombre//10
  
  while i<len(liste) :
    if liste[i]==chiffre :
      res+=1
    i+=1
  print(liste)
  print(chiffre)
  return res