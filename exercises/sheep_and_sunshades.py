"""
There are N sheep relaxing in a field. They are positioned at points with integer coordinates. Each sheep has a square sunshade, so as not to overheat. The sunshade of a sheep standing at position (X, Y) spreads out to a distance of D from (X, Y), covering a square whose middle is at (X, Y) and whose sides are of length 2D. More precisely, it covers a square with vertices in points (X − D, Y − D), (X − D, Y + D), (X + D, Y − D) and (X + D, Y + D). Sheep are in the centres of their sunshades. Sunshades edges are parallel to the coordinate axes.

Every sheep spreads out its sunshade to the same width. No two sunshades can overlap, but their borders can touch.

What is the maximum integer width D to which the sheep can spread out their sunshades?

Write a function:

def solution(X, Y)

that, given two arrays X and Y of length N denoting the positions of the sheep, returns the maximum value of D to which the sheep can spread out their sunshades. There are at least two sheep in the flock, and no two sheep share a point with the same coordinates.

Examples:

1. Given X=[0, 0, 10, 10] and Y=[0, 10, 0, 10],
the function should return 5.

2. Given X=[1, 1, 8] and Y=[1, 6, 0],
the function should return 2.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of arrays X, Y is an integer within the range [0..100,000];
no two sheep are standing in the same position.
"""
from math import inf


def solution(X, Y):
    N = len(X)
    min_distance = float(inf)

    for i in range(N):
        for j in range(i + 1, N):
            manhattan_dist = abs(X[i] - X[j]) // 2 + abs(Y[i] - Y[j]) // 2

            if manhattan_dist < min_distance:
                min_distance = manhattan_dist

    return min_distance


if __name__ == '__main__':
    # X = [0, 0, 10, 10]
    # Y = [0, 10, 0, 10]
    # X = [1, 1, 8]
    # Y = [1, 6, 0]
    X = [0, 0, 2, 3, 4, 6, 8, 8]
    Y = [4, 8, 2, 4, 8, 0, 0, 4]
    X = [0, 0, 2, 3, 4, 6, 8, 8, 4]
    Y = [4, 8, 2, 4, 8, 0, 0, 4, 3]
    print(solution(X, Y))
