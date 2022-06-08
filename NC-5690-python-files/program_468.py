def ecart(liste):
    res = None
    if len(liste) > 0:
        liste.sort()
        min, max = liste[0], liste[-1]            
        res = (min - max)* (-1)
    return res 