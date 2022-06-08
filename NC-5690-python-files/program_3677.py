def premiereOccurrenceLettre(lettre,mot):
    if lettre=='' or mot=='':
      res=None
    else:
      res=None
      for c in mot:
        if lettre==c:
          for i in range(-1,-len(mot)-1,-1):
            res=mot[i]
    return res