def nbVoyelles(mot):
  if len(mot)==0 :
    res=0
  else:
    res=0
    for elem in mot :
      if elem in 'aeiouy' :
        res=res+1
  return res