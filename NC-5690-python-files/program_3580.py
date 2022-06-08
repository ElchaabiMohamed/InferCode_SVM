def premiereOccurrenceLettre(lettre,mot):
    if len(mot)==0:
      res=None
    else:
      res=0
      for i in mot:
        if lettre==mot[i]:
          res=mot[i]
        else:
          if lettre!=mot[i]:
            res=None
    return res
  
      