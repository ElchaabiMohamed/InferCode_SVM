def premiereOccurrenceLettre(lettre,mot):
    if mot == '':
      return None
    elif lettre not in mot:
      return None
    else:
      listeoccur = []
      cpt = 0
      for c in mot:
        if c == lettre:
          listeoccur.append(cpt)
          cpt += 1
      return listeoccur[0]