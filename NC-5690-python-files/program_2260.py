def doubleLettre(mot):
    for i in range(1,len(mot)):
      if mot[i] == mot [i-1]:
        return True
      else:
        return False