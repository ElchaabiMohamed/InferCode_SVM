def moyenne(liste):
    if len(liste) == 0:
      moy = None
    else:
      res = 0
      for nb in liste:
        res = res + nb
      moy = res/len(liste)
    return moy