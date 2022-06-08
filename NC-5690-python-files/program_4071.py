def nombreSymetrique(nombre):
  res=[]
  if nombre==0:
    res=[0]
  while nombre!=0:
    res.append(nombre%10)
    nombre=nombre//10
  return res
  ok=True
  i=0
  while i<len(res)//2 and ok:
    if res[i]!=res[-i-1]:
      ok=False
    i+=1
  return ok