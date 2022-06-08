def sommeNPremiersEntiersPairs(n):
  res=0
  for i in range(n,2):
    if liste[i]:
      res=res+liste[i]
  return res