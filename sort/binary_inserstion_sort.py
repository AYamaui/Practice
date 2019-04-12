import sys
sys.path.append('../')
from search.binary_inexact_search import binary_inexact_search


# Complexity: O(n^2) for swaps / O(nlogn) for comparisons
def binary_insertion_sort(array):
    sorted_index = 1

    for i in range(1, len(array)):
        correct_position = binary_inexact_search(array[:sorted_index], array[i])

        for j in range(i, correct_position, -1):
            aux = array[j-1]
            array[j-1] = array[j]
            array[j] = aux

        sorted_index += 1


if __name__ == '__main__':
    array = [5, 2, 4, 6, 1, 3]
    binary_insertion_sort(array)
    print(array)

