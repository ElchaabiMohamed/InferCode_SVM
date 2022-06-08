def sousChaine(s1,s2):
    if len(s1)==0:
      res=True
    else:
      res=False
      if s1 in s2:
        res=True
    return res