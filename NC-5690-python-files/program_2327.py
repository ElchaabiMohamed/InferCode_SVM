def compareDates(jour1,mois1,annee1,jour2,mois2,annee2):
  result:[]
  if annee1>annee2:
    result.append(1)
    print (result)
  if annee1<annee2:
    result.append(-1)
  if annee1==annee2:
    if mois1>mois2:
      result.append(1)
      print (result)
    if mois1<mois2:
      result.append(-1)
      print (result)
    if mois1==mois2:
      if jour1>jour2:
        result.append(1)
        print (result)
      if jour1<jour2:
        result.append(-1)
        print(result)
      else:
        result.append(0)
        print (result)
  return None