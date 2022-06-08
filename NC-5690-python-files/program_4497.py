def nbVoyelles(mot):
    if len(mot)==0:
      res=0
    else:
      res=0
      for c in mot:
        if c in 'aeiouy':
          res=res+1
    return res