def premiereOccurrenceLettre(lettre,mot):
    res = mot.find(lettre)
    if res == -1: res = None    
    return res