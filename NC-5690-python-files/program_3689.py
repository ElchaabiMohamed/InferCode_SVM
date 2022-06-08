def sommeNPremiersEntiers(n):
  res= 0
  if n < 0:
    res=0
  else:
    for i in n:
      res= res + i
  return res