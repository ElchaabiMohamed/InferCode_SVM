def doubleLettre(mot):
    res = False
    c1 = ' '
    for c2 in mot:
      if c2 == c1:
        res = True
      c1 = c2
    return res