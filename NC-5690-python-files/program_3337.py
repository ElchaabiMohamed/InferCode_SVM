def maximum(l):
  res=None
  for i in range(len(l)):
    if res<i:
      res=i
  return res