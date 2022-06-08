def doubleChiffre(nombre):
  res=False
  l=[]
  chiffre=0
  i=1
  while nombre!=0 :
    chiffre=nombre%10
    l.append(chiffre)
    nombre=nombre//10
  
  while i<len(l) :
    if l[i-1]==l[i] :
      res=True
    i+=1
  
  return res