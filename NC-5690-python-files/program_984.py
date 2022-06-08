def prononcable(mot):
  res=True
  aux=''
  for c in mot:
    if c!=aux:
      res=False
    aux=c
  return res