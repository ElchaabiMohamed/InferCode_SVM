def sousChaine(s,debut,longueur):
  res = ''
  fin = debut+longueur
  if fin >len(s):
    fin = len(s)
  for i in range(debut,fin):
    res+= s[i]
  return s