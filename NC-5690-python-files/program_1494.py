def sommeNPremiersEntiersPairs(n):
    res=0
    for i in range(1,n,2):
      res=res+i
    return res