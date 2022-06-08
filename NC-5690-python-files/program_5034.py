def produitScalaire(vec1,vec2):
  if len(vec1)==[] and len(vec2)==[]:
    res=0
  else: 
    res=0
    for i in range(len(vec1) and len(vec2)):
      vec1[i]==vec2[i]
      res=res+vec1[i]*vec2[i]
  return res