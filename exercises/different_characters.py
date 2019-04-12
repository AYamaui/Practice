"""
You are given a string S consisting of N characters and an integer K. You can modify string S by removing any substring of it. A substring is defined as a contiguous segment of a string.

The goal is to find the shortest substring of S that, after removal, leaves S containing exactly K different characters.

Write a function:

class Solution { public int solution(String S, int K); }

that, given a non-empty string S consisting of N characters and an integer K, returns the length of the shortest substring that can be removed. If there is no such substring, your function should return −1.

Examples:

1. Given S = "abaacbca" and K = 2, your function should return 3. After removing substring "cbc", string S will contain exactly two different characters: a and b.

2. Given S = "aabcabc" and K = 1, your function should return 5. After removing "bcabc", string S will contain exactly one character: a.

3. Given S = "zaaaa" and K = 1, your function should return 1. You can remove only one letter: z.

4. Given S = "aaaa" and K = 2, your function should return −1. There is no such substring of S that, after removal, leaves S containing exactly 2 different characters.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..1,000,000];
string S consists only of lowercase letters (a−z);
K is an integer within the range [0..26].
"""
from math import inf
import time


def solution(S, K):
    substr_diff_values = {}
    shortest_substr = None
    shortest_substr_length = float(inf)

    for i in range(len(S)):
        for j in range(i, len(S) + 1):
            remaining_substr = S[0:i] + S[j:len(S)]

            diff_values = substr_diff_values.get(remaining_substr)

            if not diff_values:
                diff_values = len(set(remaining_substr))
                substr_diff_values[remaining_substr] = diff_values

            if diff_values == K:

                if len(S[i:j]) < shortest_substr_length:
                    shortest_substr = S[i:j]
                    shortest_substr_length = len(S[i:j])

    if shortest_substr is not None:
        return shortest_substr, shortest_substr_length

    return -1


def solution2(S, K):
    substr_diff_values = {}
    shortest_substr = None
    shortest_substr_length = float(inf)

    DP(i, j) = min(
        DP(i, k) + DP(k, j) + len(S[i:j])
        for k in range(i+1, j)
    )

    for i in range(len(S)):
        for j in range(i, len(S) + 1):
            remaining_substr = S[0:i] + S[j:len(S)]

            diff_values = substr_diff_values.get(remaining_substr)

            if not diff_values:
                diff_values = len(set(remaining_substr))
                substr_diff_values[remaining_substr] = diff_values

            if diff_values == K:

                if len(S[i:j]) < shortest_substr_length:
                    shortest_substr = S[i:j]
                    shortest_substr_length = len(S[i:j])

    if shortest_substr is not None:
        return shortest_substr, shortest_substr_length

    return -1

if __name__ == '__main__':
    start_time = time.time()
    # S = "abaacbca"
    # K = 2
    # S = "aabcabc"
    # K = 1
    # S = "zaaaa"
    # K = 1
    # S = "aaaa"
    # K = 2
    # S = "aaaa"
    # K = 0
    S = "aaaaaa"
    # K = 1
    S = "abc"
    K = 2
    print(solution(S, K))
    print(time.time() - start_time)
