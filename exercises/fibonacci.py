import time

def fibonacci(nth):

    if nth == 0:
        return 0

    if nth <= 2:
        return 1

    return fibonacci(nth - 1) + fibonacci(nth - 2)


def memoized_fibonacci(nth, memo):

    if nth in memo:
        return memo[nth]

    if nth == 0:
        return 0

    if nth <= 2:
        return 1

    fib = memoized_fibonacci((nth - 1), memo) + memoized_fibonacci((nth - 2), memo)
    memo[nth] = fib
    return fib


def bottom_up_fibonacci(nth, memo):
    fib = 0

    for k in range(nth + 1):

        if k <= 2:
            fib = 1
        else:
            fib = memo[k - 1] + memo[k - 2]
        memo[k] = fib

    return fib


if __name__ == '__main__':
    nth = 11

    start_time = time.time()
    print(fibonacci(nth))
    end_time = time.time()
    print('Fibonacci time: {}'.format(end_time - start_time))

    start_time = time.time()
    print(memoized_fibonacci(nth, {}))
    end_time = time.time()
    print('Memoized Fibonacci time: {}'.format(end_time - start_time))

    start_time = time.time()
    print(bottom_up_fibonacci(nth, {}))
    end_time = time.time()
    print('Bottom-Up Fibonacci time: {}'.format(end_time - start_time))
