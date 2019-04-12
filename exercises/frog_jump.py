"""
A small frog wants to get to the other side of the road. The frog is currently located at position X and wants to get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.

Count the minimal number of jumps that the small frog must perform to reach its target.

Write a function:

def solution(X, Y, D)

that, given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or greater than Y.

For example, given:

  X = 10
  Y = 85
  D = 30
the function should return 3, because the frog will be positioned as follows:

after the first jump, at position 10 + 30 = 40
after the second jump, at position 10 + 30 + 30 = 70
after the third jump, at position 10 + 30 + 30 + 30 = 100
Write an efficient algorithm for the following assumptions:

X, Y and D are integers within the range [1..1,000,000,000];
X ≤ Y.

"""

from math import ceil


def solution(X, Y, D):
    return ceil((Y - X) / D)


if __name__ == '__main__':
    X = 10
    Y = 85
    D = 30
    print(solution(X, Y, D))

    X = 10
    Y = 10
    D = 30
    print(solution(X, Y, D))

    X = 0
    Y = 0
    D = 30
    print(solution(X, Y, D))

    X = 10
    Y = 20
    D = 1
    print(solution(X, Y, D))

    X = 10
    Y = 20
    D = 5
    print(solution(X, Y, D))

    X = 10
    Y = 99
    D = 11
    print(solution(X, Y, D))
