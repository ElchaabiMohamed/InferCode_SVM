def moyenne(liste):
    if liste==[]:
        return None
    else:
        somme=0
        nbtermes=0
        for elem in liste:
          somme=somme+elem
          nbtermes=nbtermes+1
        moy=somme/nbtermes
        return moy