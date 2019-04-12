
#
# def binary_search(array, number, idx=0):
#
#     middle = len(array) // 2
#
#     if (len(array) == 0) or (len(array) == 1 and array[middle] != number):
#         return -1
#
#     if array[middle] == number:
#         return idx + middle
#
#     if array[middle] > number:
#         return binary_search(array[:middle], number, idx)
#     else:
#         left_idx = min([middle + 1, (len(array) - 1)])
#         return binary_search(array[left_idx:], number, left_idx + idx)


def binary_search(left, right, array, elem):

    if len(array) == 0 or (left <= right and array[left] != elem):
        return -1

    middle = (left + right) // 2

    if array[middle] == elem:
        return middle

    if elem > array[middle]:
        return binary_search(middle + 1, right, array, elem)
    else:
        return binary_search(left, middle - 1, array, elem)


if __name__ == '__main__':
    array = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    number = 16

    # binary_search(array, number)
    print(binary_search(0, len(array) - 1, array, number))
