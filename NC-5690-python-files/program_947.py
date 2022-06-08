def sommeNPremiersEntiersPairs(n):
  res= 0
  if n < 0:
    res=0
  else:
    for i in range(n+1):
      if i%2 == 0:
        res= res + i
  return res