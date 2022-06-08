def ecart(liste):
  if len(liste)!=0:
    max=liste[0]
    min=liste[0]
    for elem in liste:
      if elem>max:
        max=elem
      if elem<min:
        min=elem
    res=max-min
    return res
    