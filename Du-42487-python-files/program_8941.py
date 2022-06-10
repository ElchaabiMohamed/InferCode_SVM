def quicksort(array, a, b):
    array = _quicksort(array)

def _quicksort(array):
    if len(array) > 0:
        piv = array[0]
        less = [i for i in array if i < piv]
        print(less)
        greater = [i for i in array if i >= piv]
        return _quicksort(greater) + _quicksort(less)
    else:
        return []

