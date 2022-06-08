def semestreValide(ue1, ue2):
    if ue1 >= 10 and ue2 >= 10:
        return True
    elif ue1 >= 10:
        if ((ue1 + ue2) / 2) >= 10:
            return True
    else:
        return False