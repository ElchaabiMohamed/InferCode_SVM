def nbVoyelles(mot):
  res=0
  for c in mot:
    if c in "aeiouy":
      res=res+1
    else:
      res=0
  return res