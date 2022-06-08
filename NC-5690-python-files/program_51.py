def sousChaine(s,debut,longueur):
  res=''
  if fin>len(s):
    res=res+fin
  for i in range(debut,debut+longueur):
      res=res+s[i]
  return res