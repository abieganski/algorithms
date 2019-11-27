import math

def quicksort(array, left, right):

    # check if we've finished
    if (left >= right):
        return

    pivotValue = array[right]

    # now make sure all elements smaller than pivotValue are to the left
    # and all elements greater than pivotValue are to the right of the pivot

    lastSmallerIndex = left - 1
    for j in range(left, right):
        print(j, " : ", array)
        
        if (array[j] < pivotValue):
            lastSmallerIndex += 1
            print(lastSmallerIndex, "<->", j)

            array[lastSmallerIndex], array[j] = array[j], array[lastSmallerIndex]  # swap the current element and the one that is smaller


    # now put the pivot in the right place - between the smaller elements and the greater elements
    array[lastSmallerIndex + 1], array[right] = array[right], array[lastSmallerIndex + 1]

    pivotIndex = lastSmallerIndex + 1
    quicksort(array, left, pivotIndex - 1)
    quicksort(array, pivotIndex + 1, right)



array = [ 4, 6, 2, 9, -3, -2, 8, 5, -1, 4]
print("before: ", array)

quicksort(array, 0, len(array) - 1)
print("after: ", array)