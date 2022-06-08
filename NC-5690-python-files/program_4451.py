def premiereOccurrenceLettre(lettre,mot):
    if lettre=='' or mot=='':
      res=None
    else:
      res=None
      for c in mot:
        if lettre==c:
          res=len(mot[c])
    return res