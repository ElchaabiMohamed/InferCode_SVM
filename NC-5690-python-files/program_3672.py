def moyenne(liste):
  if liste == []:
    return None
  else:
    res=0
    for c in liste:
      res = res + c
    return res/len(liste)