def quatrePlus100(l):
  res=[]
  if (l[0]==None):
    res=None
  else:
    for i in l:
      if (i>100):
        res.append(l[i])
  return res