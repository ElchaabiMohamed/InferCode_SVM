def suiteAriGeo(liste):
  if len(liste) <= 2:
    res = True
  else:
    a = liste[1] // liste[0]
    b = liste[1] % liste[0]
    i = 2
    trouve = False
    while i <= len(liste) and trouve == False:
      if not (((liste[i] // liste[i-1]) == a) and (liste[i] % liste[i-1]) == b):
        trouve = True
      i+=1
    if trouve == False:
      res = True
    else:
      res = False
      
    return res