def bubblesort(array):
    size = len(array)
    for i in range(size):
        sorted = True

        for j in range(size - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

                sorted = False

        if sorted:
            break

    return array
