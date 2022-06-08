def qualifJO(sexe,record,nbvictoires,champion):
    res = False

    if sexe == "F" and record < 15 or sexe == "M" and record < 12 and nbvictoires >= 3 or champion == True:
         res = True
        
    
    return res