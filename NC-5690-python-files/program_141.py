def moyenne(liste):
  if liste==[]:
    return None
  else:
    S=0
    nbNotes=0
    for i in liste:
      S=S+liste[i]
      nbNotes=nbNotes+1
      
  return S/nbNotes