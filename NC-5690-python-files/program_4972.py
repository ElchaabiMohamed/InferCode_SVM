def premiereOccurrenceLettre(lettre,mot):
  if len(mot)==0:
    return None
  else:
    res=-1
    for elem in mot:
      if lettre==elem:
        res=res+1
        return res
        