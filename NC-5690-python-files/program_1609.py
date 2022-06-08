def nbOccurrencesLettre(lettre,mot):
  for i in range(len(mot)):
    if lettre in mot:
      res=res+1
    return res