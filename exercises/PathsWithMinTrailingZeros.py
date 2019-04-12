"""
Matrix A, consisting of N rows and N columns of non-negative integers, is given. Rows are numbered from 0 to N−1 (from top to bottom). Columns are numbered from 0 to N−1 (from left to right). We would like to find a path that starts at the upper-left corner (0, 0) and, moving only right and down, finishes at the bottom-right corner (N−1, N−1). Then, all the numbers on this path will be multiplied together.

Find a path such that the product of all the numbers on the path contain the minimal number of trailing zeros. We assume that 0 has 1 trailing zero.

Write a function:

def solution(A)

that, given matrix A, returns the minimal number of trailing zeros.

Examples:

1. Given matrix A below:

The picture describes the first example test.

the function should return 1. The optimal path is: (0,0) → (0,1) → (0,2) → (1,2) → (2,2) → (2,3) → (3,3). The product of numbers 2, 10, 1, 4, 2, 1, 1 is 160, which has one trailing zero. There is no path that yields a product with no trailing zeros.

2. Given matrix A below:

The picture describes the second example test.

the function should return 2. One of the optimal paths is: (0,0) → (1,0) → (1,1) → (1,2) → (2,2) → (3,2) → (3,3). The product of numbers 10, 1, 1, 1, 10, 1, 1 is 100, which has two trailing zeros. There is no path that yields a product with fewer than two trailing zeros.

3. Given matrix A below:

The picture describes the third example test.

the function should return 1. One of the optimal paths is: (0,0) → (0,1) → (1,1) → (1,2) → (2,2). The product of numbers 10, 10, 0, 10, 10 is 0, which has one trailing zero. There is no path that yields a product with no trailing zeros.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..500];
each element of matrix A is an integer within the range [0..1,000,000,000].
"""
from math import inf


def get_neighbors(x, y, N):
    neighbors = []

    if x < N - 1:
        neighbors.append((x + 1, y))
    if y < N - 1:
        neighbors.append((x, y + 1))

    return neighbors


def aux(A, x, y, product, min_product):

    product = product * A[x][y]

    if x == (len(A) - 1) and y == (len(A) - 1):

        if product < min_product[0]:
            min_product[0] = product
        return min_product

    neighbors = get_neighbors(x, y, len(A))

    for neighbor in neighbors:

        aux(A, neighbor[0], neighbor[1], product, min_product)

    return min_product


def solution(A):
    product = 1

    if not A:
        return 0

    for i in range(len(A)):
        for j in range(len(A)):
            product = product * A[i][j]

    if product == 0:
        return 1

    min_product = aux(A, x=0, y=0, product=1, min_product=[float(inf)])[0]

    if len(str(min_product)) == 1:
        return 0
    else:
        return len(str(min_product)) - len(str(min_product).rstrip('0'))


if __name__ == '__main__':
    A = [[2, 10, 1, 3], [10, 5, 4, 5], [2, 10, 2, 1], [25, 2, 5, 1]]
    print(solution(A))

    A = [[10, 1, 10, 1], [1, 1, 1, 10], [10, 1, 10, 1], [1, 10, 1, 1]]
    print(solution(A))

    A = [[10, 10, 10], [10, 0, 10], [10, 10, 10]]
    print(solution(A))

    A = []
    print(solution(A))

    A = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    print(solution(A))

    A = [[11, 11, 11], [11, 11, 11], [11, 11, 11]]
    print(solution(A))

    A = [[2, 2], [2, 2]]
    print(solution(A))

    A = [[10, 10, 10], [10, 10, 10], [10, 10, 10]]
    print(solution(A))

    A = [[2, 5, 1, 10], [10, 2, 5, 10], [10, 10, 2, 5], [10, 10, 10, 2]]
    print(solution(A))

    A = [[24]]
    print(solution(A))

    A = [[2, 5], [10, 2]]
    print(solution(A))

    A = [[2, 5, 25, 10], [10, 2, 20, 4], [2, 5, 20, 20], [100, 16, 10, 2]]
    print(solution(A))
