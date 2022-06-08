def ecart(liste):
  if liste == []:
    return None
  else:
    maximum = liste[0]
    minimum = liste[0]
    for i in range(1,len(liste)):
      if maximum < liste[i] :
        maximum = liste[i]
      elif minimum > liste[i]:
        minimum = liste[i]
    return maximum - minimum