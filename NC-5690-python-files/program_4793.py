def sousChaine(s,debut,longueur):
  res=''
  if debut<0 or debut>len(s):
    res=''
  elif (debut+longueur)>len(s):
    for i in range(debut,len(s)-debut):
      res=res+s[i]
  else:
    for i in range (debut,longueur):
      res=res+s[i]
  return res
    