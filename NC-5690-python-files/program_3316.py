def compare(chaine1,chaine2):
    i=0
    while i<len(chaine1) and i<len(chaine2) and chaine1[i]==chaine2[i]:
      i=i+1
    if chaine1[i]>chaine2[i]:
      res=1
    elif chaine1[i]<chaine2[i]:
      res=-1
    else:
      res=0
    return res