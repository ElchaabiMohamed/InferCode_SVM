def maximum(l):
  res=l[0]
  for i in range(1,len(l)):
    if i==None:
      res=None
    else:
      if res<i:
        res=i
  return res