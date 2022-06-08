def listeDecroissante(scores):
    if len(scores)==0:
      ok=True
    else:
      ok=True
      i=0
      while i<len(scores) and ok:
        if scores[i]<scores[i+1]:
          ok=False
    return ok