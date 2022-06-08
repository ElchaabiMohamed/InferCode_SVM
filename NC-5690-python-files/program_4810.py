def sommeNPremiersEntiersPairs(n):
  res=0
  for i in range(2,n+1,2):
      res=res+i
    
  return res