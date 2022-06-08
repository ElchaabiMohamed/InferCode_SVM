def sommeNPremiersEntiers(n):
    if n<0:
      res=0
    else:
      for elem in range(n+1):
        res=res+elem
    return res
        