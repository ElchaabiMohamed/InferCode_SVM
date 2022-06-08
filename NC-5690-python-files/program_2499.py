def fusion(liste1,liste2):
    if liste1==[]:
      res=liste2
    elif liste2==[]:
      res=liste1
    else:
      res=[]
      i=0
      while i<len(liste1) and i<len(liste2):
        if liste1[i]<liste2[i]:
          res=res+[min(liste1)]+[min(liste2)]
          liste1.remove(min(liste1))
          liste2.remove(min(liste2))
        elif liste1[i]>liste2[i]:
          res=res+[min(liste2)]+[min(liste1)]
          liste1.remove(min(liste1))
          liste2.remove(min(liste2))
        i=i+1
      if len(liste1)>len(liste2):
        while i<len(liste1):
          res=res+[min(liste1)]
          liste1.remove(min(liste1))
          i=i+1
      elif len(liste1)<len(liste2):
        while i<len(liste2):
          res=res+[min(liste2)]
          liste2.remove(min(liste2))
          i=i+1
    return res