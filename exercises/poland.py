"""
The weather forecast is described in an array A: for each K (0 ≤ K < N), A[K] is equal to 0 if the weather during day K favors the seaside, or 1 if the weather during that day favors the mountains.

Write a function:

def solution(A)

that, given an array A of N integers, returns the length of the longest vacation consistent with your requirements.

For example, consider array A such that:

    A[0] = 1
    A[1] = 1
    A[2] = 0
    A[3] = 1
    A[4] = 0
    A[5] = 0
    A[6] = 1
    A[7] = 1
You are free for eight days. The weather during days 2, 4 and 5 will be better for swimming, and better for trekking during the remaining days. You can start your vacation on day 1, spend five days at the seaside (three days will have perfect weather, which is more than half) and then spend two days in the mountains (both days will have perfect weather). That results in a vacation length of seven days, which is the longest possible vacation that meets your criteria, so the function should return 7.

For array A such that:

    A[0] = 1
    A[1] = 0
there is no vacation that satisfies your requirements, so the function should return 0.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer that can have one of the following values: 0, 1.
"""


def solution(A):
    start_vacation = None
    end_vacation = None
    vacation_length = 0

    if len(A) < 2:
        return 0

    for start_mountain_days in range(1, len(A)):
        mountain_days = sum(A[0:start_mountain_days])

        for i in range(start_mountain_days):

            if mountain_days < ((start_mountain_days - i) / 2):
                start_vacation = i
                break

            mountain_days -= A[i]

        if start_vacation is None:
            continue

        length_beach_vacations = start_mountain_days - start_vacation

        mountain_days = sum(A[start_mountain_days:len(A)])

        for j in range(len(A) - 1, start_mountain_days - 1, -1):

            if mountain_days > ((j - start_mountain_days + 1) / 2):
                end_vacation = j
                break

            mountain_days -= A[j]

        if end_vacation is None:
            continue

        length_mountain_vacations = end_vacation - start_mountain_days + 1

        if vacation_length < (length_beach_vacations + length_mountain_vacations):
            vacation_length = length_beach_vacations + length_mountain_vacations

    return vacation_length


if __name__ == '__main__':
    # A = [1, 1, 0, 1, 0, 0, 1, 1]
    # A = [0, 1]
    # A = [1, 0]
    # A = [0, 0, 0, 1, 1, 1, 0, 0, 1]
    # A = [0, 0, 0]
    # A = [1, 1]
    # A = []
    A = [0, 0, 0, 1, 1, 0]
    A = [1, 0, 0, 0, 0, 1]
    A = [0, 1, 0, 1, 0, 1]
    A = [1, 0, 1, 0, 1, 0]
    A = [1, 1, 0, 1, 0, 0]
    print(solution(A))
