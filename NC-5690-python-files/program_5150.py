def nbVoyelles(mot):
  if len(mot)==0:
    res=None
  else:
    res=0
    if mot in 'aeiouy':
      res=res+1
        
     
  return res