def nbOccurrencesLettre(lettre,mot):
    if len(mot) == 0:
      res = 0
    else:
      res = 0
      if lettre in range(len(mot)):
        res+=1
    return res