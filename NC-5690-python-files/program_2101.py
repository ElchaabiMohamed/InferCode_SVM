def ecart(liste):
  if len(liste)==0:
    res=None
  def maximum(liste):
    maxi=liste[0]
    for i in range(len(liste)):
      if liste[i]>maxi:
        maxi=liste[i]
  def minimum(liste):
    mini=liste[0]
    for i in range(len(liste)):
      if liste [i]<mini:
        mini=liste[i]
  res=maxi-mini
  return res