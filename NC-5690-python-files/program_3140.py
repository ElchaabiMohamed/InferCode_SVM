def nbOccurrencesLettre(lettre,mot):
    if len(mot) == 0:
      res = 0
    else:
      res = 0
      for l in mot:
        if l == lettre:
          res+=1
    return res