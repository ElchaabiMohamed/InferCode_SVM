def nbOccurrencesLettre(lettre,mot):
    res=0
    for l in mot:
      if l==lettre:
        res=res+1
    return res