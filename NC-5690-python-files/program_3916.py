def nbOccurrencesLettre(lettre,mot):
  for elem in mot:
    if elem==lettre:
      res=res+1
  return res