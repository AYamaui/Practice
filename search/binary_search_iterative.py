

def binary_search(array, number):
    left_idx = 0
    right_idx = len(array) - 1

    while left_idx <= right_idx:

        middle_idx = (left_idx + right_idx) // 2

        if array[middle_idx] == number:
            return middle_idx

        if array[middle_idx] > number:
            right_idx = middle_idx - 1
        elif array[middle_idx] < number:
            left_idx = middle_idx + 1

    return -1


if __name__ == '__main__':
    array = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    number = 9

    print(binary_search(array, number))
