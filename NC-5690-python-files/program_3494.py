def nbVoyelles(mot):
  if len(mot)==0 :
    res=0
  else:
    for elem in mot :
      if mot in 'aeiouy' :
        res=res+1
  return res