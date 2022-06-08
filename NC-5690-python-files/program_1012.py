def suiteAri(liste):
  res=True
  if len(liste)>1:
    r=liste[1]-liste[0]
    res=verifSuiteAriGeo(liste,1,r)
  return res