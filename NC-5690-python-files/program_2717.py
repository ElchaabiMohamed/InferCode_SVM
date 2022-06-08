def jourNuit(heure):
    res = ""
    if heure>24 :
        res = "l'heure saisie est invalide" 
    return res
    
jourNuit(28)   