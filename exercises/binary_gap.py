"""
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

Write a function:

def solution(N)

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
"""


def solution(N):
    longest_binary_gap = 0
    binary_gap = 0

    for char in bin(N)[2:]:

        if char == '0':
            binary_gap += 1
        if char == '1' and binary_gap > 0:

            if binary_gap > longest_binary_gap:
                longest_binary_gap = binary_gap

            binary_gap = 0

    return longest_binary_gap


if __name__ == '__main__':
    N = 9
    print(solution(N))
    N = 529
    print(solution(N))
    N = 20
    print(solution(N))
    N = 15
    print(solution(N))
    N = 32
    print(solution(N))
    N = 0
    print(solution(N))
    N = 1
    print(solution(N))
    N = 170
    print(solution(N))
    N = 1296
    print(solution(N))
    N = 2561
    print(solution(N))
    N = 1280
    print(solution(N))
