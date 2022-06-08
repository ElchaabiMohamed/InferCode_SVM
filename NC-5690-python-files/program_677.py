def sommeNPremiersEntiers(n):
  if n<0:
    return 0
  else:
    res=0
    for i in range (len(n)):
      res=res+n[i]
  return res
      
    