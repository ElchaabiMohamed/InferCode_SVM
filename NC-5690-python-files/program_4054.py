def sommeNPremiersEntiersPairs(n):
  res=0
  for e in range(N+1):
    if e%2==0:
      res=res+e
  return res