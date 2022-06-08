def sommeNPremiersEntiersPairs(n):
    res=0
    for n in range(1,n+1):
      if n%2==0:
        res=res+n
    return res