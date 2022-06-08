def nbOccurrencesLettre(lettre,mot):
  n = 0
  for i in mot:
    if lettre == i:
      n+=1
  return n