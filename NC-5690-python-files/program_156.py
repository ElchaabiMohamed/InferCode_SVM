def prononcable(mot):
  if len(mot)==0:
    return None
  elif len(mot)<4:
    return True
  else:
    cpt=0
    laLettrePrecedenteEstUneVoyelle = (mot[0] in 'aeiouy')
    for i in mot :
      if (i in 'aeiouy') == laLettrePrecedenteEstUneVoyelle:
        cpt+=1
        if cpt == 4:
          return False
      else:
        cpt = 1
        laLettrePrecedenteEstUneVoyelle = not laLettrePrecedenteEstUneVoyelle 
    return True