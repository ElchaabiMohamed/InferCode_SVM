def sommeNPremiersEntiersPairs(n):
    res=0
    for i in range(n,2,-2):
      res=res+i
    return res