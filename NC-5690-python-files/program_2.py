def nbOccurrencesLettre(lettre,mot):
    res=0
    for i in range(0,len(mot)):
      if lettre in mot:
        res=res+1
      return res