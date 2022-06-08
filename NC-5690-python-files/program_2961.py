def nbVoyelles(mot):
  if len(mot)==0 :
    res=0
  else:
    for elem in mot :
      if (['a','e','i','o','u','y']) in mot :
        res=res+1
    return res