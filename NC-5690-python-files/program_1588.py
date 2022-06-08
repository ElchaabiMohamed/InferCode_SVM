def sommeNPremiersEntiers(n):
  if n<=0:
    res=0
  else:
    for elem in n:
      res=elem+n 
  return res