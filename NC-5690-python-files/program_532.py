def distribution(liste,n):
  res=[]
  for i in range(0,n):
    b=1
    for a in liste:
      if a==i:
        res[i]=i+b
        b=b+1
    res=res+res[i]