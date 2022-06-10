
def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 1/2
    total_radius = r1 + r2

    if distance < total_radius:
        return True
    else:
        return False
