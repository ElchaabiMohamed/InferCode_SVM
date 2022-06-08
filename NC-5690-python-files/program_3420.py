def premiereOccurrenceLettre(lettre,mot):
  if len(mot)==0:
    pos=None
  else:
    cpt=0
    for elem in mot:
      cpt=cpt+1
      if lettre==elem:
        pos=elem[i]
      else:
        pos=None
        
  return pos