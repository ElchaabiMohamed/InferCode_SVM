def sommeNbPairs(liste):
  res = 0;
  for i in liste:
    if (i%2==0):
      res+=i
  return res