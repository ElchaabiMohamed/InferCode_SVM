def jourNuit(heure):
  if not(0<=heure<24):
    return "l'heure saisie est invalide"
  else:
    res='on est '
    if(5<=heure<12):
      res+='le matin '
    elif(12<=heure<17):
      res+="l'après-midi "
    elif(17<=heure<21):
      res+='le soir '
    else:
      res+='la nuit '
    res += 'et il fait '
    if(6<=heure<18):
      res+='jour'
    else:
      res+='nuit'
    return res