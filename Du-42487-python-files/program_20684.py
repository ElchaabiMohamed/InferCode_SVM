def quicksort(array, a, b):
    array = _quicksort(array)

def _quicksort(array):
    less = []
    greater = []
    equal = []
    if len(array) > 0:
        piv = array[0]
        less = [i for i in array if i < piv]
        greater = [i for i in array if i > piv]
        equal = [i for i in array if i == piv]
        return _quicksort(greater) + equal + _quicksort(less)
    else:
        return []

