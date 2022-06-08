def maximum(liste):
  if liste == []:
    return None
  else:
    maximum = liste[0]
    for i in range(1,len(liste)):
      if maximum < liste[i]:
        maximum = liste[i]
    return maximum