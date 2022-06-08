def sousChaine(s,debut,longueur):
  res=""
  if longueur>=len(s):
    longueur=longueur-(longueur-len(s))
  for i in range(debut,longueur):
    res=res+s[i]
  return res
