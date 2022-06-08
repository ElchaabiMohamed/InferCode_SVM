def sommeNPremiersEntiersPairs(n):
  res=0
  for x in range(n+1):
    if x%2==0:
      res=res+x
  return res