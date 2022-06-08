def produitScalaire(vec1,vec2):
  res=0
  for i in range(len(vec1)):
    aux=vec1[i]*vec2[i]
    res=res+aux
  return res