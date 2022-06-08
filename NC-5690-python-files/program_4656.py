def prononcable(mot):
  if len(mot)<4:
    return True
  else:
    cpt=0
    laLettrePrecedenteEstUneVoyelle = (mot[0] in 'aeiouy')
    for i in mot :
      if (i in 'aeiouy') == laLettrePrecedenteEstUneVoyelle:
        cpt+=1
        if cpt == 3:
          return False
      else:
        cpt = 0
        laLettrePrecedenteEstUneVoyelle = not laLettrePrecedenteEstUneVoyelle 
    return True