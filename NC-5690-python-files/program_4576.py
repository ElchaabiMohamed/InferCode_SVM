def sousChaine(s,debut,longueur):
  res=''
  if debut+longueur>len(s):
    res=debut+longueur
  else:
    res=fin
    for i in range(debut,debut+longueur): 
      fin=fin+s[i]
  return res