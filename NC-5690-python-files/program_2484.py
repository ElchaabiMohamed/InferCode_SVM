def rendezVous(debut1,fin1,debut2,fin2):
    if debut1>debut2:
      if debut1>fin2:
        res=False
      elif debut1<fin2:
        res=True
      else:
        res=False
    elif debut1<debut2:
      if fin1>debut2:
        res=True
      elif fin1<debut2:
        res=False
      else:
        res=False
    else:
      if fin1>fin2 or fin1<fin2:
        res=True
      else:
        res=False
    return res