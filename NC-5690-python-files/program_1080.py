def produitScalaire(vec1,vec2):
    res=0
    for i in range(4):
      p1=vec1(i)
      p2=vec2(i)
      res=res+p1*p2
    return 