def sommeNPremiersEntiersPairs(n):
  res=0
  for e in range(n+1):
    if e%2==0:
      res=res+e
  return res