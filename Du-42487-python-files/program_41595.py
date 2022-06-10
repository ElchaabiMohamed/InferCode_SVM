def union(a, b):
    i = 0
    c = []
    while i < len(a):
        if a != b:
           c = (a, b)
           return c
           i = i + 1   
    
