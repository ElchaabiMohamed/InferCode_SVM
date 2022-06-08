def nbOccurrencesLettre(lettre,mot):
    res=0
    for i in range(1,len(mot)):
      if lettre in mot:
        res=res+1
      return res