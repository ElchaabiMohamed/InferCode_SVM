def sousChaine(s,debut,longueur):
    res=''
    fin=debut+longueur
    if fin>len(mot):
      fin=len(mot)
    for i in range (debut,fin):
      res=res+mot[i]
    return res