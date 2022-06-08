def sommeNPremiersEntiersPairs(n):
  res=0
  for i in range(0,n+1,1):
    if i%2==0:
      res=res+i
  return res