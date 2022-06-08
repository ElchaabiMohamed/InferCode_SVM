def sommeNPremiersEntiersPairs(n):
  res=1
  for elem in range(2,n+1,2):
    res=res+elem
  return res
    