def nbVoyelles(mot):
  if len(mot)==0:
    return 0
  else:
    for elem in mot:
      res=0
      if elem== mot[0] or mot[4] or mot[8] or mot[14] or mot[20] or mot[24]:
        res=res+1
        return res