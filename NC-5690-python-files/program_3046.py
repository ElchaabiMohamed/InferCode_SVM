def nbOccurrencesLettre(lettre,mot):
    res=0
    for i in mot:
      if lettre in mot:
        res=res+1
      return res