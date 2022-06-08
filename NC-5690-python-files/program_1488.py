def jourNuit(heure):
    if heure>24:
      res="l'heure saisie est invalide"
    else:
      if 5<=heure<12:
        res="on est le matin et il fait jour"
      else:
        if 12<=heure<17:
          res="on est l'après-midi et il fait jour"
        else:
          if 17<=heure<21:
            res="on est le soir et il fait nuit"
          else:
            if 21<=heure<24:
              res="on est la nuit et il fait nuit"
    return res
  