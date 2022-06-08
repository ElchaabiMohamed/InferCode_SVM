def suiteAriGeo(liste):
    if liste==[] or len(liste)==1:
      ok1=True
    else:
      ok1=True
      ctePrec=liste[1]-liste[0]
      cteAct=None
      i=2
      while i<len(liste) and ok1:
        cteAct=liste[i]-liste[i-1]
        if liste[0]+i*ctePrec!=cteAct:
          ok1=False
        ctePrec=cteAct
        i+=1
    if liste==[] or len(liste)==1:
      ok2=True
    elif 0 in liste:
      if liste[0]!=0:
        ok2=True
      while 0 in liste:
        liste.remove(0)
      if liste==[]:
        ok2=True
      else:
        ok2=False
    else:
      ok2=True
      i=1
      while i<len(liste) and ok2:
        cte=liste[i]/liste[i-1]
        if liste[0]*cte**i!=liste[i]:
          ok2=False
        i+=1
    ok3=True
    trouve=False
    i=0
    while i>-len(liste)-1 and not trouve:
      if liste[-i-1]!=0 and liste[-i-2]!=0:
        cteGeo=(liste[-i-1])//liste[-i-2]
        if cteGeo!=0:
          cteAri=liste[-i-1]%cteGeo
          trouve=True
      i-=1
    i=0
    if cteGeo==1:
      ok3=False
    else:
      while i<len(liste) and ok3:
        if (cteGeo**i)*(liste[0]-cteAri/(1-cteGeo))+cteAri/(1-cteGeo)!=liste[i]:
          ok3=False
        i+=1
    return ok1 or ok2 or ok3