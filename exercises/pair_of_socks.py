import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    picked_socks = {}
    pairs = 0

    for sock in ar:
        picked_socks.setdefault(sock, 0)
        picked_socks[sock] += 1

    for sock, amount in picked_socks.items():
        pairs += amount // 2

    return pairs


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input())
    n = 9

    # ar = list(map(int, input().rstrip().split()))
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

    result = sockMerchant(n, ar)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
