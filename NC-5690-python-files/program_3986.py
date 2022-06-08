def sommeNPremiersEntiersPairs(n):
  if n<=0:
    res=0
  else:
    for n in liste:
      if n%2==0:
        res=(n*(n+1))/2
  return res