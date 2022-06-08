def sousChaine(s,debut,longueur):
  res=''
  if debut<len(s) or debut>len(s):
    res=''
  elif (debut+longueur)>len(s):
    for i in range(debut,len(s)-debut):
      res=res+s[i]
  return res
    