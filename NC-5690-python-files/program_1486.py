def nombreSymetrique(nombre):
    decomp=stockerChiffres(nombre);
    return listeSymetrique(decomp)

def listeSymetrique(l):
    res=True
    i=0
    while i<len(l)//2 and res:
        if l[i]!=l[-(i+1)]:
            res=False
        i+=1
    return res

def stockerChiffres(nombre):
    res=[]
    decomp=nombre
    while decomp!=0:
        res+=[decomp%10]
        decomp=decomp//10
    if res==[]: #cas de 0
        res=[0]
    return res