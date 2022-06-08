def stockerChiffres(nombre):
    res=[]
    decomp=nombre
    while decomp!=0:
      res+=[decomp%10]
      decomp=decomp//10
    if res==[]:
      res+=[0]
    return res