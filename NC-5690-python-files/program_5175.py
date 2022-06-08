def listedecroissante(scores):
  ok=True
  if len(scores)==0:
    ok=True
  i=0
  while i<len(scores)-1:
    if scores[i]<scores[i+1]:
      ok=False
    i+=1
  return ok