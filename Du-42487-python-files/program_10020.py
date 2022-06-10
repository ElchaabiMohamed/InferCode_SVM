def quicksort(l, a, b):
    def _quicksort(array):
        if not array:
            return []
        else:
            pivot = array[0]
            less = [x for x in array     if x <  pivot]
            more = [x for x in array[1:] if x >= pivot]
            return quicksort(less) + [pivot] + quicksort(more)

    l = _quicksort(l)
    

