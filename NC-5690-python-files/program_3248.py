def suiteGeo(liste):
  if liste==[] or len(liste)==1:
    ok = True
  elif 0 in liste:
    ok = False
  else:
    ok = True
    i = 1
    cte = liste[i]/liste[i-1]
    while i<len(liste) and ok:
      if liste[i]/liste[i-1]!=cte:
        ok = False
      i+=1
  return ok 