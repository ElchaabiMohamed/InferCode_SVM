def premiereOccurrenceLettre(lettre,mot):
  if len(mot)==0:
    return None
  else:
    res=0
    for elem in mot:
      if lettre==elem:
        res=res+1
    return res
        