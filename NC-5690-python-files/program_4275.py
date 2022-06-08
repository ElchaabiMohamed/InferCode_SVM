def sousChaine(s,debut,longueur):
  res=''
  if debut+longueur>len(s):
    fin=len(s)
  else:
    fin=debut+longueur  
  for i in range(debut,fin):
    res=res+s[i]
  return res