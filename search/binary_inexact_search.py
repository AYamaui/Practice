from math import ceil


def binary_inexact_search(array, number):
    array_size = len(array) - 1
    left = 0
    right = array_size

    while True:

        middle = ceil((left + right) / 2)

        if left == right or left > right:
            left = min(left, array_size)

            if array[left] <= number:
                return left + 1
            else:
                return left

        if array[middle] > number:
            right = middle - 1
        else:
            left = middle + 1


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6]
    correct_position = binary_inexact_search(array, 7)
    print(correct_position)
    correct_position = binary_inexact_search(array, 0)
    print(correct_position)
    correct_position = binary_inexact_search(array, 4.5)
    print(correct_position)
