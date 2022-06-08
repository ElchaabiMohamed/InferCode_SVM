def nombreSymetrique(nombre):
  if nombre==0:
    res=[0]
  else:
    res=[]
    while nombre!=0:
      res.append(nombre%10)
      nombre//=10
  if res==[]:
    ok=True
  else:
    ok=True
    i=0
    while i<len(res) and ok:
      if res[i]!=res[-i-1]:
        ok=False
      i+=1
    return ok