def listeDecroissante(scores):
  ok=True
  i=0
  while i<len(scores)-1 and ok:
    if scores[i]<scores[i+1]:
      ok=False
    i+=1
  else:
    if len(scores)==[]:
      ok=True
  return ok