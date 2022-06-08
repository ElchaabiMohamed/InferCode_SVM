def sommeNPremiersEntiersPairs(n):
    if n<0:
      res=0
    else:
      res=0
      for x in range(n):
        if x%2==0:
          res=res+x
    return res
  