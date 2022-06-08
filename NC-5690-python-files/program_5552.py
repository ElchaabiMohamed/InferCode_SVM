def maximum(l):
  if len(l)==0:
    res=l[0]
    for i in range(1,len(l)):
      if res<i:
        res=i
  else:
    res=None
    return res