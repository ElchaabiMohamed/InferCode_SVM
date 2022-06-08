def nbOccurrencesLettre(lettre,mot):
  if len(mot)==0:
    return None
  else:
    res=liste[0]
    cpt=0
    for elem in mot:
      if lettre in mot:
        cpt=cpt+1
      return cpt

    