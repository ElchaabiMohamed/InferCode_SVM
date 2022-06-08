def qualifJO(sexe,record,nbvictoires,champion):
    res = False
    if (sexe == "F" or sexe == "M") and record > 0 and nbvictoires > 0 and type(champion) == bool:
        
        if champion == True: res = True

        record_need = 12

        if sexe == "F":
            record_need = 15
        print(record_need)
        if record < record_need and nbvictoires >= 3:
            res = True
    else:
        return "Tricheur"
        
    
    return res