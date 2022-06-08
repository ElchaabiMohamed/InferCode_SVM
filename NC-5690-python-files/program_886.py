def premiereOccurrenceLettre(lettre,mot):
    if lettre=='' or mot=='':
      res=None
    else:
      res=None
      for c in range(-1,-len(mot)-1,-1):
        if lettre==c:
          res=mot[c]
    return res