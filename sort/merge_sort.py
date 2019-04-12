#
#
# def merge_iterative(array_1, array_2):
#     sorted_array = []
#     array_1_size = len(array_1)
#     array_2_size = len(array_2)
#     i = j = 0
#
#     while i < array_1_size or j < array_2_size:
#
#         if i < array_1_size and j >= array_2_size:
#             sorted_array.extend(array_1[i:])
#             break
#         elif j < array_2_size and i >= array_1_size:
#             sorted_array.extend(array_2[j:])
#             break
#         elif array_1[i] <= array_2[j]:
#             sorted_array.append(array_1[i])
#             i += 1
#         else:
#             sorted_array.append(array_2[j])
#             j += 1
#
#     return sorted_array
#
#
# def merge_recursive(array1, array2):
#
#     if len(array1) < 1:
#         return array2
#
#     if len(array2) < 1:
#         return array1
#
#     if array1[0] < array2[0]:
#         return [array1[0]] + merge_recursive(array1[1:], array2)
#     else:
#         return [array2[0]] + merge_recursive(array1, array2[1:])
#
#
# def merge_sort(array):
#
#     if len(array) <= 1:
#         return array
#     else:
#         middle = len(array) // 2
#         sorted_array_1 = merge_sort(array[:middle])
#         sorted_array_2 = merge_sort(array[middle:])
#         # return merge_iterative(sorted_array_1, sorted_array_2)
#         return merge_recursive(sorted_array_1, sorted_array_2)
#
#
# if __name__ == '__main__':
#     array = [12, 28, 3, 6, 10, 1]
#
#     sorted_array = merge_sort(array)
#     print(sorted_array)


# Second try

# Complexity O(lgn) in terms of time / O(n) in auxiliary space (assignment of sorted list into variables)
# def merge_sort(array):
#
#     if len(array) <= 1:
#         return array
#
#     middle = (len(array) // 2)
#
#     array1 = merge_sort(array[:middle])
#     array2 = merge_sort(array[middle:])
#
#     return merge(array1, array2)
#
# Complexity O(n) / O(n) in auxiliary space (concatenation of lists)
# def merge(array1, array2):
#
#     if not array1:
#         return array2
#     if not array2:
#         return array1
#
#     if array1[0] < array2[0]:
#         return [array1[0]] + merge(array1[1:], array2)
#     else:
#         return [array2[0]] + merge(array1, array2[1:])
#
# Overall complexity T(n) = O(C1 + 2T(n/2) + C2*n) (divide + recursion + merge)
#
# if __name__ == '__main__':
#     array = [12, 28, 3, 6, 10, 1]
#     # array = [5, 2, 4, 6, 1, 3]
#     # array = [6, 5, 4, 3, 2, 1]
#     # array = [2]
#
#     sorted_array = merge_sort(array)
#     print(sorted_array)

