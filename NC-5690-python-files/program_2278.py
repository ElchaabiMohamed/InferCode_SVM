def sommeNbPairs(liste):
    res = 0
    for nb in liste:
      if nb%2 == 0:
        res = res + nb
    return res