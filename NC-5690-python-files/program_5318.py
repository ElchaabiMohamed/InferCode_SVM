def nbVoyelles(mot):
  res=0
  for elem in mot:
    if elem in mot==["a","e","i","o","u","y"]:
      res=res+1
  return res