"""
A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

For example, consider array A such that:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
We can split this tape in four places:

P = 1, difference = |3 − 10| = 7
P = 2, difference = |4 − 9| = 5
P = 3, difference = |6 − 7| = 1
P = 4, difference = |10 − 3| = 7
Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

For example, given:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−1,000..1,000].
"""


def solution(A):
    sum_left = A[0]
    sum_right = sum(A[1:])
    min_diff = abs(sum_left - sum_right)

    for i in range(1, len(A) - 1):
        sum_left += A[i]
        sum_right -= A[i]
        diff = abs(sum_left - sum_right)

        if diff < min_diff:
            min_diff = diff

    return min_diff


if __name__ == '__main__':
    A = [3, 1, 2, 4, 3]
    print(solution(A))
    A = [-1, -2, 1]
    print(solution(A))
    A = [1, 1]
    print(solution(A))
    A = [-1, -1]
    print(solution(A))
    A = [-1, -5]
    print(solution(A))
    A = [5, 56]
    print(solution(A))
    A = [1, 1]
    print(solution(A))
    A = [-12, 90]
    print(solution(A))
    A = [-12, -43, -19, -78]
    print(solution(A))
    A = [34, 90, 12, 11]
    print(solution(A))
    A = [100, 2, 5, 6, 80, 30]
    print(solution(A))
    A = [-100, 2, 5, 6, 80, 30]
    print(solution(A))
    A = [23, 15, 12, 25]
    print(solution(A))
    A = [-23, -15, 12, 25]
    print(solution(A))
