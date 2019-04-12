

# Complexity: O(n^2) for swaps / O(n^2) for comparisons
def insertion_sort(array):

    for i in range(1, len(array)):
        j = i
        while j >= 1 and array[j-1] > array[j]:
            aux = array[j-1]
            array[j-1] = array[j]
            array[j] = aux
            j -= 1

    return array


if __name__ == '__main__':
    array = [5, 2, 4, 6, 1, 3]
    insertion_sort(array)
    print(array)

