def quicksort(array, b, c):
    less = []
    greater = []
    equal = []
    if len(array) > 0:
        piv = array[0]
        less = [i for i in array if i < piv]
        greater = [i for i in array if i > piv]
        greater = [i for i in array if i == piv]
        array = less + greater + equal
