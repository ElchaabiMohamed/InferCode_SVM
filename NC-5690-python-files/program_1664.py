def sommeNPremiersEntiers(n):
  if n<0:
    res=0
  else:
    for i in range(n):
      res=res+[i]
  return res