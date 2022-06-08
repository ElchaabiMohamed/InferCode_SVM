def sommeNbPairs(l):
  res=0
  for x in l:
    if x%2==0:
      res=res+x
      
  return res