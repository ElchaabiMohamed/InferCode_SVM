def premiereOccurrenceLettre(lettre,mot):
  if len(mot)==0:
    pos=None
  else:
    res=-1
    for elem in mot:
      if lettre!=elem:
        pos=pos+1
      else:
        pos=pos+1
        return pos