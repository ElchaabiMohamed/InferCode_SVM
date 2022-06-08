def jourNuit(heure):
  while heure < 0 or heure > 24 :
    return "l'heure saisie est invalide"
  if heure >= 6 and heure <= 18 :
    nuit_jour = "jour"
  else:
    nuit_jour = "nuit"
  if heure >= 5 and heure < 12:
    moment = "le matin"
  elif heure >= 12 and heure < 17:
    moment = "l'après-midi"
  elif heure >= 17 and heure < 21:
    moment = "le soir"
  else:
    moment = "la nuit"
  return "on est {} et il fait {}".format(moment,nuit_jour)