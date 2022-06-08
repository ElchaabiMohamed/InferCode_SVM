def nbVoyelles(mot):
  if len(mot)==0:
    res=0
  else:
    res=0
    for lettre in mot:
      if lettre in ["a","e","i","o","u","y"]:
        res=res+1
  return res
  
      
  

 