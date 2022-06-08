def doubleLettre(mot):
    res=False
    for i in range(len(mot)):
      if mot[i]==mot[i+1]:
        res=True
    return res
      