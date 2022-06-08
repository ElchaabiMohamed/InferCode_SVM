def sommeNPremiersEntiers(n):
  if n<0:
    res=0
  else:
    for i in range(n+1):
      res=res+i
  return res