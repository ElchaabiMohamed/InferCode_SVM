def rendezVous(debut1,fin1,debut2,fin2):
  res=True
  if debut1<=debut2:
    if fin1<debut2:
      if fin1<debut2:
      	res=False
  if debut2<=debut1:
    if fin2<fin1:
      if fin2<debut1:
      	res=False
  return res