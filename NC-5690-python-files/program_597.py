def sousChaine(s,debut,longueur):
    res=''
    fin=deb+longueur
    if fin>len(mot):
      fin=len(mot)
    for i in range (deb,fin):
      res=res+mot[i]
    return res