def sousChaine(s,debut,longueur):
  res=''
  cpt=0
  for i in range (debut,len(s)):
    res=res+s[i]
    cpt=cpt+1
    if cpt==longueur:
      return res

