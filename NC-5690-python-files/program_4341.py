def produitScalaire(vec1,vec2):
    if vec1==[] or vec2==[]:
      res=0
    else:
      res=0
      for i in len(vec1):
        res+=vec1[i]*vec2[i]
    return res
      