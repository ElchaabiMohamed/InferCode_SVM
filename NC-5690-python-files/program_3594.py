def maximum(l):
  res=None
  for i in range(1,len(l)):
    if res<i:
      res=i
  return res