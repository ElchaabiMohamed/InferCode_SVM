def sousChaine(s,debut,longueur):
  res=""
  fin=debut+long
  if fin>len(s):
    fin=len(s)
  for i in range(debut,fin):
    res=res+s[i]
  return None