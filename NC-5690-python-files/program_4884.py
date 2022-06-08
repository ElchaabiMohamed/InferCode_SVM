def nbVoyelles(mot):
  if len(mot)==0:
    res=None
  else:
    for mot in "aeiouy":
      res=res+1
  
  return res