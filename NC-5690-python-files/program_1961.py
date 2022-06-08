def nombreSymetrique(nombre):
  while nombre!=0:
    res.append(nombre%10)
    nombre=nombre//10
  res=True
  i=0
  while i<len(nombre)//2 and res:
    if nombre[i]!=nombre[-i-1]:
      res=False
    i+=1
  if res==0:
    res=0
  return res