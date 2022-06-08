def sousChaine(s,debut,longueur):
  res=""
  fin=deb+long
  if fin>len(s):
    fin=len(s)
  for i in range(deb,fin):
    res=res+s[i]
  return None