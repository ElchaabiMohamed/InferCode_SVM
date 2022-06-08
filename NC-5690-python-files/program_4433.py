def nbOccurrencesLettre(lettre,mot):
  if len(mot)==0:
    res=0
  else:
    cpt=0
    for elem in mot:
      if lettre==elem:
        cpt=cpt+1
    res=cpt
  return res

    