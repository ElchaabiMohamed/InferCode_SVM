from statistics import mean

def moyenne(liste):
    res = None
    if len(liste) > 0:
        res = mean(liste)
    return res