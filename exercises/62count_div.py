"""
Write a function:

def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.
"""

""" 
Didn't pass following cases:
 - A = 100, B=123M+, K=2
 - A = 0, B = MAXINT, K in {1,MAXINT}
 - A, B, K in {1,MAXINT}
"""

import time


def solution(A, B, K):
    number = A
    divisible_counter = 0
    divisor = A // K

    while number <= B:

        if number % K == 0:
            divisible_counter += 1

        divisor += 1
        number = divisor * K

    return divisible_counter


def solution_v2(A, B, K):
    number = A
    divisible_counter = 0
    divisor = A // K

    if number % K == 0:
        divisible_counter += 1

    divisor += 1
    number = divisor * K

    while number <= B:
        divisible_counter += 1
        divisor += 1
        number = divisor * K

    return divisible_counter


if __name__ == '__main__':
    A = 6
    B = 11
    K = 2
    print(solution(A, B, K))

    A = 0
    B = 11
    K = 3
    print(solution(A, B, K))

    A = 0
    B = 0
    K = 3
    print(solution(A, B, K))

    A = 0
    B = 1
    K = 3
    print(solution(A, B, K))

    A = 0
    B = 9
    K = 3
    print(solution(A, B, K))

    start_time = time.time()
    A = 12
    B = 144
    K = 11
    print(solution(A, B, K))
    print(time.time() - start_time)

    start_time = time.time()
    A = 12
    B = 144
    K = 11
    print(solution_v2(A, B, K))
    print(time.time() - start_time)

    start_time = time.time()
    A = 50
    B = 110000000000
    K = 13
    print(solution(A, B, K))
    print(time.time() - start_time)

    start_time = time.time()
    A = 50
    B = 110000000000
    K = 13
    print(solution_v2(A, B, K))
    print(time.time() - start_time)

    start_time = time.time()
    A = 100
    B = 110000000000
    K = 2
    print(solution(A, B, K))
    print(time.time() - start_time)

    start_time = time.time()
    A = 100
    B = 110000000000
    K = 2
    print(solution_v2(A, B, K))
    print(time.time() - start_time)
