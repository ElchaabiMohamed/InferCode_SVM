def nbVoyelles(mot):
  if len(mot)==0:
    res=0
  else:
      i="a,e,i,o,u,y"
      if i in mot:
        res=res+1
  return res             

      
    