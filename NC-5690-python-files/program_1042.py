def nbOccurrencesLettre(lettre,mot):
  cpt=0
  for elem in mot:
    if lettre==elem:
      cpt=cpt+1
  res=cpt
  return res

    