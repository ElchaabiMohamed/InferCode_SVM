def premiereOccurrenceLettre(lettre,mot):
  if len(liste)==0:
    return None
  cpt=0
  for i in range (len(liste)):
    if lettre in mot:
      cpt=liste[i]
  return cpt