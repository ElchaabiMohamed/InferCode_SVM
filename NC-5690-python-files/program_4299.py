def nombreSymetrique(nombre):
  nr=[]
  if nombre==0:
    nr=[0]
  while nombre!=0:
    nr.append(nombre%10)
    nombre=nombre//10
  res=True
  i=0
  while i<len(nr)//2 and res:
    if nr[i]!=nr[-i-1]:
      res=False
    i+=1
  return res