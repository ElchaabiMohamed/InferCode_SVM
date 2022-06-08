def distribution(liste,n):
  res=[]
  for i in range(0,n):
    b=1
    res.append(0)
    for a in liste:
      if a==i:
        res[i]=b
        b=b+1
  return res