def listeSymetrique(l):
    i=0
    ok=True
    while i<len(liste) and ok==True:
      if liste[i]!=liste[-i-1]:
        ok=False
      i=i+1
    return ok 