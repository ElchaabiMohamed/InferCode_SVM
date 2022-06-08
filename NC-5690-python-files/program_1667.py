def premiereOccurrenceLettre(lettre,mot):
  if len(mot)==0:
    pos=None
  else:
    for elem in mot:
      if lettre==elem:
        pos=mot[i]
      else:
        pos=None
        
  return pos