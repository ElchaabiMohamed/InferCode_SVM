def premiereOccurrenceLettre(lettre,mot):
    res = None
    if len(mot) > 0:
        res = mot.index(lettre)
    return res