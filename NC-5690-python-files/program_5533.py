def nombrePair(n):
  res=0
  for x in range(len(n)):
    if x%2==0:
      res=True
    else:
      res=False
  return res