def premiereOccurrenceLettre(lettre,mot):
  if len(mot)==0:
    pos=None
  else:
    for elem in mot:
      if lettre==elem:
        pos=elem
      else:
        pos=None
        
  return pos