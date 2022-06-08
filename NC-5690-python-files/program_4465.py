def doubleLettre(mot):
    res=False
    for i in range(len(mot)):
      if (mot[i+1]==mot[i]):
        res=True
    return res
      