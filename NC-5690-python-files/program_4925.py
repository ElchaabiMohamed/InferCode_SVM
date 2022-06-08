def compareDates(jour1,mois1,annee1,jour2,mois2,annee2):
    if annee1==annee2:
      if mois1==mois2:
        if jour1==jour2:
          return 0
        elif jour1<jour2:
          return -1
        else:
          return 1
      elif mois1<mois2:
        return -1
      else:
        return 1
    elif annee1<annee2:
      return -1
    else:
      return 1