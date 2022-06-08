def premiereOccurrenceLettre(lettre,mot):
    if len(mot)==0:
      res=None
    else:
      res=0
      for elem in mot:
        if lettre==elem:
          res=mot[elem]
        else:
          if lettre!=mot[elem]:
            res=None
    return res
  
      