def quicksort(array, b, c):
    less = []
    greater = []
    equal = []
    if len(array) > 0:
        piv = array[0]
        less = [i for i in array if i < piv]
        greater = [i for i in array if i > piv]
        equal = [i for i in array if i == piv]
        quicksort(greater, b,c)
        quicksort(less, b, c)
        array = greater + equal + less
