def nombrePair(n):
  res=True
  for elem in range(n):
    if elem%2!=0:
      res=False
  return res