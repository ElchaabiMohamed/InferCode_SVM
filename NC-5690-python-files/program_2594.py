def sommeNPremiersEntiersPairs(n):
  res=0
  for i in range(len(1,n+1)):
    if liste[i]%2==0:
      res=res+liste[i]
  return res