def nbOccurrencesLettre(lettre,mot):
    if len(mot)==0:
      cpt=None
    else:
      cpt=0
      for elem in mot:
        if elem==lettre:
          cpt=cpt+1
    return cpt
  