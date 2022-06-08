def elemGeo(n,u0,q):
    res=0
    x=0
    while x<=n:
      res=u0*q**n
      x+=1
    return res