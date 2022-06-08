def nbVoyelles(mot):
  res=0
  if mot==0:
    res=None
  else:
    if mot in 'aeiouy':
      for mot in 'aeiouy':
        res=res+1
  
     
  return res