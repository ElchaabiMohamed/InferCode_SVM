def nombreSymetrique(nombre):
  res=[]
  if nombre==0:
    res=[0]
  while nombre!=0:
    res.append(nombre%10)
    nombre=nombre//10
  return res
  res=True
  i=0
  while i<len(l)//2 and res:
    if l[i]!=l[-i-1]:
      res=False
    i+=1
  return res