def nbOccurrencesLettre(lettre,mot):
    cpt=0
    for elem in mot:
      if elem==lettre:
        cpt=cpt+1
    return cpt
  