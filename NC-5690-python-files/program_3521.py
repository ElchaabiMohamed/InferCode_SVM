def verifSuiteAriGeo(liste,a,b):
  i=0
  c=True
  while i<(len(liste)+1) and c:
    if liste[i+1]!=a*liste[i]+b:
      c=False
    i=i+1
  return c