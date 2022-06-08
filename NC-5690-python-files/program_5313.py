def premiereOccurrenceLettre(lettre,mot):
    if len(mot)==0:
      res=None
    else:
      res=0
      for c in mot:
        if c==lettre:
          res=mot[c]
        else:
          if lettre!=mot[elem]:
            res=None
    return res
  
      