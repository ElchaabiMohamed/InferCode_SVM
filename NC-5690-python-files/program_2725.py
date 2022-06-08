def nombreSymetrique(nombre):
  ok=True
  l=[]
  chiffre=0
  i=0
  j=-1
  while nombre!=0 :
    chiffre=nombre%10
    l.append(chiffre)
    nombre=nombre//10
  
  while i<(len(l)/2) and ok :
    if l[i]!=l[j] :
      ok=False
    i+=1
    j-=1
  
  return ok