def nombreSymetrique(nombre):
  res.append(nombre%10)
  res=True
  i=0
  while i<len(l)//2 and res:
    if l[i]!=l[-i-1]:
      res=False
    i+=1
  return res