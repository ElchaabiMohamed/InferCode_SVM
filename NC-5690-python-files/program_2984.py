def suiteAriGeo(liste):
  if len(liste)<3:
    ok=True
  else:
    ok=True
    ecart1=liste[1]-liste[0]
    ecart2=liste[2]-liste[1]
    a=ecart2/ecart1
    b=-a*liste[0]+liste[1]
    if a*liste[2]+b!=liste[3]:
      ok=False
  return ok