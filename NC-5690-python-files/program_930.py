def produitScalaire(vec1,vec2):
    if len(vec1)==0 or len(vec2)==0:
      res=0
    else:
      res=0
      for i in range(len(vec1)) and i in range(len(vec2)):
        res=res+vec1[i]*vec2[i]
    return res 