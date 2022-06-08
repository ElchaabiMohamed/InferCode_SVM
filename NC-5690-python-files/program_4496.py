def nbOccurrencesLettre(lettre,mot):
    if len(mot) == 0:
      res = 0
    else:
      if lettre in range(len(mot)):
        res+=1
    return res