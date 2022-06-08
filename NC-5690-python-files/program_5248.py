def maximum(liste):
    res = None
    if len(liste) > 0:
        liste.sort()
        res = liste[0]
    return res