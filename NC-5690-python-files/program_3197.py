def moyenne(liste):
  if liste==[]:
    return None
  else:
    S=0
    nbNotes=0
    for elem in liste:
      S=S+elem
      nbNotes=nbNotes+1
      
  return S/nbNotes