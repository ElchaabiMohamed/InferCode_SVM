def compareDates(j1,m1,a1,j2,m2,a2):
    if a1<a2:
      res=-1
    elif a1>a2:
      res=1
    elif m1<m2:
      res=-1
    elif m1>m2:
      res=1
    elif j1<j2:
      res=-1
    elif j1>j2:
      res=1
    else:
      res=0
    return res