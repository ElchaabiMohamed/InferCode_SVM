def nbOccurrencesLettre(lettre,mot):
  res=0
  for elem in mot:
    if lettre==elem:
      res+=1
  return res