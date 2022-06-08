def quatrePlus100(liste):
  res = []
  c = 0
  while c <len(liste) and len(res) < 4:
    if liste[c] > 100 :
      res = res + [liste[c]]
    c=c+1
  return res 