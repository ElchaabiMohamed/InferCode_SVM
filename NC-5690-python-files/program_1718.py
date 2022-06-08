def nbVoyelles(mot):
  Voyelles=["a","e","i","o","u","y"]
  res=0
  for l in mot:
    if l in Voyelles:
      res=res+1
  return res