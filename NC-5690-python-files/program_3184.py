def ecart(liste):
  if len(liste)==0:
    res=None
  else:
    grand=liste[0]
    petit=liste[0]
    for i in range(len(liste)):
      if liste[i]>grand:
        grand=liste[i]
      if liste[i]<petit:
        petit=liste[i]
    res=grand-petit
    return res