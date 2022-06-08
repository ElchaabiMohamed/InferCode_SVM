def nbOccurrencesLettre(lettre,mot):
    if len(mot)==0:
      res=0
    else:
      res=0
      for i in range(len(mot)):
        if mot[i]==lettre:
          res+=1
    return res