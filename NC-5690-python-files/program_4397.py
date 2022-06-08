def premiereOccurrenceLettre(lettre,mot):
  if len(mot)==0:
    return None
  cpt=0
  for i in range (len(mot)):
    if lettre in mot:
      cpt=lettre[i]
  return cpt