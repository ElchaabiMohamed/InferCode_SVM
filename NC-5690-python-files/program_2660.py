def qualifJO(sexe,record,nbvictoires,champion):
    if sexe == 'M':
        if record < 12 and nbvictoires >= 3 or champion:
            return True
        else:
            return False
    elif sexe == 'F':
        if record < 15 and nbvictoires >= 3 or champion:
            return True
        else:
            return False