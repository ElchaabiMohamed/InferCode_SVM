def nbVoyelles(mot):
  res=0
  for c in mot:
    if c in "aeiouy":
      res=res+1
  return res