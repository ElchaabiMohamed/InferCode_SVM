def fusion(liste1,liste2):
    if liste1==[]:
      res=liste2
    elif liste2==[]:
      res=liste1
    else:
      res=liste1+liste2
    res.sort()
    return res