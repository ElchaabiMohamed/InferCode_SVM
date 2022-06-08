def premiereOccurrenceLettre(lettre,mot):
  if len(mot)==0:
    pos=None
  else:
    for i in range(len(mot)):
      if lettre==i:
        pos=i
      else:
        pos=None
        
  return pos