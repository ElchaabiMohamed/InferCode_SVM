def sousChaine(s,debut,longueur):
    fin=debut+longueur
    if debut+longueur>len(s):
        fin=len(s)
    for i in range(debut,fin):
        res=res+s[i]
    return res