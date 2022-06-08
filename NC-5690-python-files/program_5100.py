def suiteAriGeo(liste):
  if len(liste)<3:
    ok=True
  else:
    ok=True
    ecart1=liste[1]-liste[0]
    ecart2=liste[2]-liste[1]
    if ecart1==0 or ecart2==0:
      a=1
    else:
      a=ecart2/ecart1
    b=-a*liste[0]+liste[1]
    i=1
    while i<len(liste)-1 and ok:
      if a*liste[i]+b!=liste[i+1]:
        ok=False
      i+=1
  return ok