def selectionsort(array):
    for i in range(len(array)):
        for j in range(i, len(array)):
            if(array[i] > array[j]):
                array[i], array[j] = array[j], array[i]