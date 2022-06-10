def quicksort(array, a, b):
    array = _quicksort(array)

def _quicksort(array):
    if len(array) <= 1:
        return array
    else:
        piv = array[0]
        less = []
        greater = []
        for i in array:
            if i < piv:
                less = less + [i]
            else:
                greater = greater + [i]
        less = _quicksort(less)
        more = _quicksort(more)
        return less + more


