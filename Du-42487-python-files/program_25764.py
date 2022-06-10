def quicksort(array, a, b):
    array = _quicksort(array)

def _quicksort(array):
    if len(array) > 0:
        piv = array[0]
        less = []
        greater = []
        for i in array:
            if i < piv:
                less += i
            else:
                greater += i
        return _quicksort(greater) + _quicksort(less)
    else:
        return []

