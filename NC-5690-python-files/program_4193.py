def maximum(l):
  res=l[0]
  for i in range(len(l)):
    if res<i:
      res=i
  return res