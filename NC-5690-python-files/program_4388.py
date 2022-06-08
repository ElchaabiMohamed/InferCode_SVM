def prononocable(mot):
    consonne=True
    cpt=0
    i=0
    while cpt<=3 and i<len(mot):
        if mot[i] in 'aeiouy':    #on observe une voyelle
            if consonne :
                consonne=False
                cpt=1         #on débute une nouvelle séquence de voyelles
            else:
                cpt+=1        #on poursuit la séquence de voyelles
        else: #on suppose qu'une non voyelle est une consonne
            if consonne:
                cpt+=1        #on poursuit une séquence de consonnes
            else:
                consonne=True
                cpt=1         #on débute une nouvelle séquence de consonnes
        i+=1
    return cpt<=3