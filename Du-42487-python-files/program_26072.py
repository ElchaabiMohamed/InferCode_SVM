def minimum(line):
    smallest = line[0]
    for c in line:
        if c < smallest:
            smallest = c
    return smallest
