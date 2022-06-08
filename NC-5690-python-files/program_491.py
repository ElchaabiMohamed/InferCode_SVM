def sousChaine(s,debut,longueur):
  res=""
  fin=debut+longueur
  if fin>len(s):
    fin=len(s)
  else:
    for i in range(len(fin)):
      res=res+fin[i]
  return res