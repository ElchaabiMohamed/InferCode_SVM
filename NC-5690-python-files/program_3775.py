def nextConway(s):
    liste=[]
    while s!=0:
      liste+=s%10
      s//=10
    if len(liste)==1:
      cw=[1,1]
    elif len(liste)==2:
      cw=[2,1]
    else:
      nliste=[0]
      for i in range(len(liste)):
        nliste=[liste[i]]+nliste
      cw=[]
      cpt=1
      for i in range(len(nliste)-1):
        if nliste[i]==nliste[i+1]:
          cpt+=1
        else:
          cw+=[cpt]
          cw+=[nliste[i]]
          cpt=1
    res=0
    for i in range(len(cw)):
      res+=cw[-i-1]*10**abs(-i)
    return res