def nombrePair(n):
  res=True
  for elem in range(n):
    if elem%10!=0:
      res=False
  return res