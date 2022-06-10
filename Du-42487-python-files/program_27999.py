def union(a, b):
    i = 0
    while i < len(a):
        if a != b:
           c = (a, b) - (a + b)
           return c
           i = i + 1   
    
