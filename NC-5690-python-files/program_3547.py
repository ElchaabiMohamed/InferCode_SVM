def jourNuit(heure):
  """
  cette fonction a pour objectif d'indiquer dans quelle partie de la journée on est et s'il fait jour ou nuit
  paramètre: 
    heure : de type int représente l'heure
  résultat:un str qui indique dans quelle partie de la journée on est et s'il fait jour ou nuit
  """
  if heure>24 or heure<0:
    res="l'heure saisie est invalide"
  #on gère le moment de la journée
  else:
    if heure<5 or heure>=21:
      res="on est la nuit"
    elif heure<12:
      res="on est le matin"
    elif heure<17:
      res="on est l'après-midi"
    else:
      res="on est le soir"
    #on gère s'il fait jour ou nuit
    if heure<6 or heure>=18:
      res=res+" et il fait nuit"
    else:
      res=res+" et il fait jour"
  return res

  #test de la fonction jourNuit
  assert jourNuit(9)=="on est le matin et il fait jour","Problème avec jourNuit(9)"
  assert jourNuit(15)=="on est l'après-midi et il fait jour","Problème avec jourNuit(9)"
  assert jourNuit(29)=="l'heure saisie est invalide","Problème avec jourNuit(9)"