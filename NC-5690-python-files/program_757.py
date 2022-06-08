def prononcable(mot):
  if mot=='':
    res=True
    return res
  else:
    res=True
    aux=''
    for c in mot:
      if c==aux:
        res=False
      aux=c
  return res