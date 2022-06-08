def moyenne(liste):
    if len(liste) == 0:
      moy = None
    else:
      res = 0
      nb = 0
      for nb in liste:
        res = res + nb
        nb+=1
      moy = res/nb
    return moy