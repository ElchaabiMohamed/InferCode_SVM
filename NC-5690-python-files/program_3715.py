def jourNuit(heure):
  """
  Fonction qui affiche le moment de la journée
  paramètres:
  heure:une heure entre 0 et 24
  renvoie une chaîne de caractère décrivant le moment de la journée et s'il fait jour ou nuit
  """
  
  #on gère le moment de la journée
  if heure<0 or heure>24:
    res="l'heure saisie est invalide"
  else:
    if heure<5 or heure>=21:
      res="on est la nuit"
    elif heure<12:
      res="on est le matin"
    elif heure<17:
      res="on est l'après midi"
    else:
      res="on est le soir"
    #on gère s'il fait jour ou nuit
    if heure<6 or heure>=18:
      res=res+" et il fait nuit"
    else:
      res=res+" et il fait jour"
    return res
    