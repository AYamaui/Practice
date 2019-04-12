def find_quantities(N):
    count = 0
    str_N = str(N)
    A = N

    for idx in range(len(str_N) - 1, -1, -1):

        if str_N[idx] == '4':
            A -= 10 ** count

        count += 1

    B = N - A

    return A, B


if __name__ == '__main__':

    n_test_cases = int(input())
    # test_cases = [4, 940, 4444]

    # for idx, test_case in enumerate(test_cases):
    for test_case in range(n_test_cases):
        N = int(input())
        A, B = find_quantities(N)

        print('Case #{}: {} {}'.format(test_case + 1, A, B) + '\n')


