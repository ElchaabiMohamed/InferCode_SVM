def produitScalaire(vec1,vec2):
  res=0
  produit=0
  i=0
  while i<len(vec1):
    produit=vec1[i]*vec2[i]
    res=res+produit
    i=i+1
  return res