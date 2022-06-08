def nbOccurrencesLettre(lettre,mot):
  res=0
  for elem in mot:
    if elem==lettre:
      res+=1
  return res