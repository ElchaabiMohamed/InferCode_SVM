def prononcable(mot):
  if len(mot)<4:
    return True
  else:
    voyelles = 'aeiouy'
    cpt=0
    laLettrePrecedenteEstUneVoyelle = True
    for i in mot :
      if i in 'aeiouy' == laLettrePrecedenteEstUneVoyelle:
        cpt+=1
        if cpt == 4:
          return False
      else:
        cpt = 0
        laLettrePrecedenteEstUneVoyelle = not laLettrePrecedenteEstUneVoyelle 
    return True