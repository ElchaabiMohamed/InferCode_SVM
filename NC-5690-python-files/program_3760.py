def suiteAriGeo(liste):
  ok=True
  i=0
  j=0
  R=0
  Q=0
  if len(liste)<=2 :
    ok=True
  else :
    while j<(len(liste)-2):
      if liste[0]==0 :
        Q=1
      elif (liste[j+1]-liste[j])==(liste[j+2]-liste[j+1]) :
        Q=1
        R=(liste[1]-liste[0])
      elif (liste[j+1]/liste[j])==(liste[j+2]/liste[j+1]) :
        Q=(liste[1]/liste[0])
        R=0
      else : 
        if (liste[1]/liste[0])<(liste[2]/liste[1]) :
          Q=(liste[1]//liste[0])
        else :
          Q=liste[2]//liste[1]
          R=liste[2]-(Q*liste[1])
      j+=1
      
    while i<(len(liste)-1) and ok :
      if liste[i+1]!=Q*liste[i]+R :
        ok=False
      i+=1
  return ok